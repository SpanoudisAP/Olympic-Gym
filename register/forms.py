from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


#Registration Form
class newuserform(UserCreationForm): 
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Profile update Form
class userprofileupdateform(UserChangeForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),
        required=False,
        label="New password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}),
        required=False,
        label="Confirm new password",
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        # Make sure passwords match
        if password and password2:
            if password != password2:
                raise ValidationError("The passwords do not match.")
            
            # Validate password strength using Django's validators
            validate_password(password, self.instance)
        
        return cleaned_data
