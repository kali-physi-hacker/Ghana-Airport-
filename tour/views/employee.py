from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from tour.models.employee import Employee
from tour.models.category import Category
from tour.forms.employee import EmployeeForm


def list_employees(request):
    template = "employees/list.html"
    employees = Employee.objects.all()
    context = {"employees": employees, "list_employee_active": "active", "employee_show": "show",
               "employee_active": "active"}
    return render(request, template, context)


def add_employee(request):
    template = "employees/add.html"
    form = EmployeeForm()
    categories = Category.objects.all()
    context = {"form": form, "categories": categories, "add_employee_active": "active", "employee_show": "show",
               "employee_active": "active"}
    return render(request, template, context)


def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST or None)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Added Successfully")
            return redirect("list_employees")
        else:
            messages.error(request, "Employee Creation Failed!")
            return redirect("add_employee")


def edit_employee(request, pk):
    template = "employees/edit.html"
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.GET or None, instance=employee)
    context = {"form": form}
    return render(request, template, context)


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