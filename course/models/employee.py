import os, random

from django.db import models
from django.utils import timezone

from django_countries.fields import CountryField, Country

from course.models.category import Category


def get_filename_ext(filepath):
    file_base = os.path.basename(filepath)
    file_name, file_ext = os.path.splitext(file_base)
    return file_name, file_ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9485739387934)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "profile_pics/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


# Create your models here.
class Employee(models.Model):
    
    default_country = Country(code='GH')

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150, blank=True, null=True)
    other_name = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    mobile_number = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_enrollment = models.DateTimeField(null=True, blank=True)
    station = models.CharField(max_length=120, null=True, blank=True)
    course_name = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField(null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.first_name
