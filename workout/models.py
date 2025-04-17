from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Workout(models.Model):
    
    WORKOUT_TYPES = [
        # Workout type 
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),

    ]

    DIFFICULTY_LEVELS = [
        # Workout dif level
        (1, 'Beginner'),
        (2, 'Easy'),
        (3, 'Moderate'),
        (4, 'Hard'),
        (5, 'Advanced'),
        
    ]

    custom_name = models.CharField(max_length=50, blank=True, null=True) # To add a Name for the workout 
    type = models.CharField(max_length=20, choices=WORKOUT_TYPES) # choose a type from the options 
    duration = models.PositiveIntegerField(help_text="Duration in minutes") #Duration of the workout
    difficulty = models.IntegerField(choices=DIFFICULTY_LEVELS) # Difficulty level

    likes = models.PositiveIntegerField(default=0) # Like 
    dislikes = models.PositiveIntegerField(default=0) # Dislike 


class WorkoutVote(models.Model):
    VOTE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    vote = models.CharField(max_length=7, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'workout')  # one vote per user per workout

def __str__(self):
    return f"{self.user} voted {self.vote} on {self.workout}"


    def __str__(self):
        return self.name