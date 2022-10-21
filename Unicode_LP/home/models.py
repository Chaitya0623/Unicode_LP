from asyncio.windows_events import NULL
from tkinter import Image
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.TextField()
    Married = models.BooleanField(blank=True)
    Birthday = models.DateTimeField()
    Image = models.ImageField(null=True, blank=True, upload_to='static/')

    def __str__(self):
        return self.Name

class Foreign(models.Model):
    User = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Age = models.IntegerField(default=NULL)
    
    def __str__(self):
        return self.Age