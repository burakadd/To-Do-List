from django.urls import path

from ToDo.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(
        template_name='ToDo/index.html',
        success_url="/",
    ),
         name='index',),
]
