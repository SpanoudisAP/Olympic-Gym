from django.db import models
from django.contrib.auth.models import User
from workout.models import Workout
from exercises.models import Exercise 

# Create your models here.



class TrainingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.workout.custom_name} ({self.date.date()})"
    
    

class TrainingExerciseLog(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, related_name='exercise_logs')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise.name} - {self.reps} reps x {self.sets} sets"