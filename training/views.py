from django.shortcuts import render, redirect
from .models import TrainingSession
from workout.models import Workout
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def my_training_sessions(request):
    sessions = TrainingSession.objects.filter(user=request.user).order_by('-date')
    return render(request, 'training/my_sessions.html', {'sessions': sessions})