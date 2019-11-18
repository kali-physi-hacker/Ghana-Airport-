from django.shortcuts import render 

from tour.models.employee import Employee


def list_employees(request):
    template = "employees/list.html"
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, template, context)