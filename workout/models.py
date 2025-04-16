from django.db import models

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


    def __str__(self):
        return self.name