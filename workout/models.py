from django.db import models

# Create your models here.

class Workout(models.Model):
    
    WORKOUT_TYPES = [

        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),

    ]

    DIFFICULTY_LEVELS = [

        (1, 'Beginner'),
        (2, 'Easy'),
        (3, 'Moderate'),
        (4, 'Hard'),
        (5, 'Advanced'),
        
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    difficulty = models.IntegerField(choices=DIFFICULTY_LEVELS)


    def __str__(self):
        return self.name