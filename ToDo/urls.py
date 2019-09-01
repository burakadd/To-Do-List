from django.urls import path

from ToDo.views import MainView, RegisterView

urlpatterns = [
    path('', MainView.as_view(), name='index', ),
    path('signup', RegisterView.as_view(), name='register'),
]
