from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ToDo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('text', )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
