from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'type', 'duration', 'difficulty']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
        }

