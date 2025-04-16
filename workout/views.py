from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import WorkoutForm
from .models import Workout

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
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def workout_list(request):
    workout = Workout.objects.all()
    
    # Filtering
    workout_type = request.GET.get('type')
    min_duration = request.GET.get('min_duration')
    max_duration = request.GET.get('max_duration')
    difficulty = request.GET.get('difficulty')

    if workout_type:
        workout = workout.filter(type=workout_type)
    if min_duration:
        workout = workout.filter(duration__gte=min_duration)
    if max_duration:
        workout = workout.filter(duration__lte=max_duration)
    if difficulty:
        workout = workout.filter(difficulty=difficulty)

    return render(request, 'workout/workout_list.html', {'workout': workout})

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

# Here starts the staff stuff :)

def staff_required(user):
    return user.is_staff


#Staff portal view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_passes_test(staff_required)
def staff_portal(request):
    return render(request, 'staff/portal.html')