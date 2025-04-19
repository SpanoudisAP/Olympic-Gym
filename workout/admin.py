from django.contrib import admin
from .models import Workout
from exercises.models import Exercise

# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    filter_horizontal = ('exercises',)

admin.site.register(Workout, WorkoutAdmin)