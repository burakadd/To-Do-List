from django.shortcuts import render, redirect
from  django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

# Create your views here.


def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'ToDo/index.html', context)


@require_POST
def addToDo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

