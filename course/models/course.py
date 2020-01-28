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

    def notify(self):
        time_diff = self.start_date - timezone.now().date() # - self.start_date 
        alert = 0
        if (time_diff.days > 0) & (time_diff.days <= 5):
            alert = 1
        return alert

    def duration_in_days(self):
        difference = self.end_date - self.start_date 
        value = 0
        if difference.days > 0:
            value = difference.days
        return value

    def duration_used(self):
        difference = timezone.now().date() - self.start_date
        value = 0
        if difference.days > 0:
            value = difference.days
        return value 