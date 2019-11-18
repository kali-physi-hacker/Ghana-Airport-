from django.db import models

from tour.models.category import Category

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name