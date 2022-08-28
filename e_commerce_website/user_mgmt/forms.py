from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User


User = get_user_model()

class CreateUserForm(UserCreationForm):
    gender = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=100)
    contact = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'gender', 'email', 'contact', 'password1', 'password2']
