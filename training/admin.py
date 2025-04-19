from django.contrib import admin
from .models import TrainingSession, TrainingExerciseLog

# Register your models here.

admin.site.register(TrainingSession)
admin.site.register(TrainingExerciseLog)