from django import forms

from ToDo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('text', )
