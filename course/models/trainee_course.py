from django.db import models 

from course.models.trainee import Trainee


class TraineeCourse(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    trainee = models.ManyToManyField(Trainee)

    def __str__(self):
        return self.name