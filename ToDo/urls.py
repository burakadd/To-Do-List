from django.urls import path, include

from ToDo.models import Todo
from ToDo.views import MainPage
from . import views

urlpatterns = [
    path('', MainPage.as_view(
        template_name='ToDo/index.html',
        success_url="/",
    ),
         name='index',),
    # path('addToDo', views.addToDo, name='addToDo'),

]
