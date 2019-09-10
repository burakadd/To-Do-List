from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView

from .models import Todo
from .forms import TodoForm, RegisterForm


class MainView(CreateView):
    form_class = TodoForm
    template_name = 'ToDo/index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        return {
            'todo_list': Todo.objects.all(),
            'form': self.form_class
        }


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    template_name = 'ToDo/register.html'

    def form_valid(self, form):
        form.save()

        user = authenticate(
            request=self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )

        login(self.request, user)
        return super().form_valid(form)



class DeleteToDo(DeleteView): model = Todo
    template_name = 'ToDo/delete_todo.html'
    success_url = reverse_lazy('mysite:companies')

