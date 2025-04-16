from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['custom_name', 'type', 'duration', 'difficulty']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}),
            'custom_name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
        }

