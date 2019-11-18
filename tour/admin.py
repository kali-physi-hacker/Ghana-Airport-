from django.contrib import admin

from tour.models.category import Category
from tour.models.employee import Employee
from tour.models.trip import Trip

# Register your models here.
admin.site.register(Category)
admin.site.register(Employee)
admin.site.register(Trip)