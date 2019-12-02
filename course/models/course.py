from django.db import models 

from course.models.employee import Employee


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name