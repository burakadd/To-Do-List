from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
