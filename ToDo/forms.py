from django import forms

from ToDo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('text', )

    # smtext = forms.CharField(
    #     max_length=40,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'make zverkova happy',
    #             'aria-label': 'ToDo',
    #             'aria-describedby': 'add-btn'
    #         }
    #     )
    # )
