from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(
        label=("first_name"),
        widget=forms.TextInput,
    )
    last_name = forms.CharField(
        label=("last_name"),
        widget=forms.TextInput,
    )
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']

class CreateTask(ModelForm):
    class Meta:
        model = TodoApp
        fields = ('title','complete')
        #exclude = ['user']
