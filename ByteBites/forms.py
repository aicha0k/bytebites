from django import forms
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def confirmpass(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)