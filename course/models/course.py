from django.db import models 
from django.utils import timezone

from django_countries.fields import CountryField

from course.models.employee import Employee


class Course(models.Model):
    name = models.CharField(max_length=150)
    country = CountryField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    description = models.CharField(max_length=500, null=True, blank=True)
    employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name