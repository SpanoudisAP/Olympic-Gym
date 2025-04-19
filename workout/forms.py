from django import forms
from .models import Workout, Exercise, TrainerQuestion

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['custom_name', 'type', 'duration', 'difficulty', 'exercises']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}),
            'custom_name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'exercises': forms.CheckboxSelectMultiple()
        }



class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'equipment', 'description']


class TrainerQuestionForm(forms.ModelForm):
    class Meta:
        model = TrainerQuestion
        fields = ['question']