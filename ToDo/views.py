from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import FormView
from django.views.generic.base import ContextMixin

from .models import Todo
from .forms import TodoForm
# Create your views here.


# def index(request):
#     todo_list = Todo.objects.order_by('id')
#
#     form = TodoForm()
#
#     context = {'todo_list': todo_list, 'form': form}
#
#     return render(request, 'ToDo/index.html', context)


class MainPage(FormView):
    form_class = TodoForm
    context = {

    }

    def form_valid(self, form):
        form.save()
        return super(MainPage, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return {
            'todo_list': Todo.objects.all(),
            'form': self.form_class
        }


# @require_POST
# def addToDo(request):
#     form = TodoForm(request.POST)
#
#     if form.is_valid():
#         new_todo = Todo(text=request.POST['text'])
#         new_todo.save()
#
#     return redirect('index')
