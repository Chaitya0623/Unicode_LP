from django.db import models

# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=75)
    content = models.TextField()
    image = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.eventName