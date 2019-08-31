from django.views.generic import FormView

from .models import Todo
from .forms import TodoForm


class MainPage(FormView):
    form_class = TodoForm

    def form_valid(self, form):
        form.save()
        return super(MainPage, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return {
            'todo_list': Todo.objects.all(),
            'form': self.form_class
        }
