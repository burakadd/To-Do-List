from django.views.generic import CreateView

from .models import Todo
from .forms import TodoForm


class MainPage(CreateView):
    form_class = TodoForm

    def get_context_data(self, **kwargs):
        return {
            'todo_list': Todo.objects.all(),
            'form': self.form_class
        }
