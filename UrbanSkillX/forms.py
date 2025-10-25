from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
    
    class Media:
        css = {
            'all': ('UrbanSkillX/form-style.css',)
        }

class CustomLoginForm(AuthenticationForm):
    
    class Media:
        css = {
            'all': ('UrbanSkillX/form-style.css',)
        }