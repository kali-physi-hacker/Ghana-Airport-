from django.db import models 


class Trip(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)