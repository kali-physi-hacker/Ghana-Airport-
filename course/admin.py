from django.contrib import admin

from course.models.category import Category
from course.models.employee import Employee
from course.models.course import Course
from course.models.trainee import Trainee

# Register your models here.
admin.site.register(Category)
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Trainee)