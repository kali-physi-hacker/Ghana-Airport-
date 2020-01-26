from django.db import models 

from django.utils import timezone


class Notification(models.Model):
    title = models.CharField(max_length=50, unique=True)
    message = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title 