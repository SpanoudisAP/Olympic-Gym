from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import WorkoutForm, ExerciseForm, TrainerQuestionForm
from .models import Workout, WorkoutVote, Exercise, TrainerQuestion
from django.db.models import Q
from django.utils.timezone import now

# Create your views here.


#Homepage view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'home.html')


#Index/Workout page view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request, 'workout/workout.html')

#Here starts a workout filtering

def workout_list(request):
    workout = Workout.objects.all()
    
    user_votes = {}
    
    # Filtering

    query = request.GET.get('s')
    workout_type = request.GET.get('type')
    min_duration = request.GET.get('min_duration')
    max_duration = request.GET.get('max_duration')
    difficulty = request.GET.get('difficulty')

    if query:
        workout = workout.filter(Q(custom_name__icontains=query))
    if workout_type:
        workout = workout.filter(type=workout_type)
    if min_duration:
        workout = workout.filter(duration__gte=min_duration)
    if max_duration:
        workout = workout.filter(duration__lte=max_duration)
    if difficulty:
        workout = workout.filter(difficulty=difficulty)
        user_votes = {}
    if request.user.is_authenticated:
        votes = WorkoutVote.objects.filter(user=request.user)
        user_votes = {vote.workout_id: vote.vote for vote in votes}

    return render(request, 'workout/workout_list.html', { 'workout': workout, 'user_votes': user_votes})



# Like/dISLIKE 1 per user
@login_required
def vote_workout(request, workout_id, vote_type):
    workout = get_object_or_404(Workout, id=workout_id)

    if vote_type not in ['like', 'dislike']:
        return redirect('workout_list')

    vote, created = WorkoutVote.objects.get_or_create(user=request.user, workout=workout)

    if vote.vote != vote_type:
        vote.vote = vote_type
        vote.save()

    # Count and update workout vote totals
    workout.likes = WorkoutVote.objects.filter(workout=workout, vote='like').count()
    workout.dislikes = WorkoutVote.objects.filter(workout=workout, vote='dislike').count()
    workout.save()

    return redirect('workout_list')


# Here starts the form for the workout
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'workout/create_workout.html', {'form': form})


# ask questions
@login_required
def ask_question(request):
    if request.method == 'POST':
        form = TrainerQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_list')
    else:
        form = TrainerQuestionForm()
    return render(request, 'workout/ask_question.html', {'form': form})


def question_list(request):
    questions = TrainerQuestion.objects.all().order_by('-created_at')
    return render(request, 'workout/question_list.html', {'questions': questions})

# Staff Stuff happen here do not look 


@staff_member_required
def staff_portal(request):
    return render(request, 'staff_portal/home.html')

@staff_member_required
def manage_exercises(request):
    exercises = Exercise.objects.all()
    return render(request, 'staff_portal/manage_exercises.html', {'exercises': exercises})


@staff_member_required
def manage_workouts(request):
    workouts = Workout.objects.all()
    return render(request, 'staff_portal/manage_workouts.html', {'workouts': workouts})


# Told you not to look. Workout edit and delete are here

#edit
@staff_member_required
def edit_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('manage_workouts')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'staff_portal/edit_workout.html', {'form': form, 'workout': workout})

#delete
@staff_member_required
def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('manage_workouts')
    return render(request, 'staff_portal/delete_workout.html', {'workout': workout})


# Here starts the Exersises edit and delete

#create
@staff_member_required
def create_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_exercises')
    else:
        form = ExerciseForm()
    return render(request, 'staff_portal/create_exercise.html', {'form': form})

#edit
@staff_member_required
def edit_exercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('manage_exercises')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'staff_portal/edit_exercise.html', {'form': form, 'exercise': exercise})

#delete
@staff_member_required
def delete_exercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('manage_exercises')
    return render(request, 'staff_portal/delete_exercise.html', {'exercise': exercise})


#questions
@staff_member_required
def answer_question(request, pk):
    question = get_object_or_404(TrainerQuestion, pk=pk)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer:
            question.answer = answer
            question.answered_by = request.user
            question.answered_at = now()
            question.save()
            return redirect('question_list')
    return render(request, 'workout/answer_question.html', {'question': question})