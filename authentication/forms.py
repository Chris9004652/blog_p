from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model= CustomUser
        fields= UserCreationForm.Meta.fields + ('email','bio','birth_date')
        
class CustomAuthenticationForm(AuthenticationForm):
    pass
        