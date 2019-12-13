from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django_countries.fields import countries

from course.models.employee import Employee
from course.models.category import Category
from course.forms.employee import EmployeeForm


@login_required
def list_employees(request):
    template = "employees/list.html"
    employees = Employee.objects.all()
    context = {"employees": employees, "list_employee_active": "active", "employee_show": "show",
               "employee_active": "active"}
    return render(request, template, context)


@login_required
def add_employee(request):
    template = "employees/add.html"
    form = EmployeeForm()
    categories = Category.objects.all()
    context = {"form": form, "categories": categories, "add_employee_active": "active", "employee_show": "show",
               "employee_active": "active", "countries": countries}
    return render(request, template, context)


@login_required
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Added Successfully")
            return redirect("list_employees")
        else:
            messages.error(request, "Employee Creation Failed!")
            return redirect("add_employee")


@login_required
def edit_employee(request, pk):
    template = "employees/edit.html"
    employee = get_object_or_404(Employee, pk=pk)
    employee.trip_set.count()
    form = EmployeeForm(request.GET or None, instance=employee)
    context = {"form": form}
    return render(request, template, context)


@login_required
def update_employee(request, pk):
    if request.method == "POST":
        employee = get_object_or_404(Employee, pk=pk)
        form = EmployeeForm(request.POST or None, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Information Updated Successfully")
            return redirect("list_employees")
        else:
            messages.error(request, "Employee Update Failed")
            return redirect("edit_employee")