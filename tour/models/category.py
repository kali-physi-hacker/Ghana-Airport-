from django.db import models 


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name