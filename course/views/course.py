from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from course.models.course import Course
from course.models.employee import Employee
from course.forms.course import CourseForm


# Create your views here.
@login_required
def home(request):
    template = "index.html"
    context = {}
    return render(request, template, context)


@login_required
def list_course(request):
    template = "course/list.html"
    courses = Course.objects.all()
    context = {"courses": courses, "list_course_active": "active", "course_show": "show", "course_active": "active"}
    return render(request, template, context)


@login_required
def add_course(request):
    template = "course/add.html"
    form = CourseForm()
    employees = Employee.objects.all()
    context = {"form": form, "employees": employees, "add_course_active": "active", "course_show": "show", "course_active": "active"}
    return render(request, template, context)


@login_required
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST or None)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "course Added Successfully")
            return redirect("list_course")
        else:
            messages.error(request, "course Creation Failed")
            return redirect("add_course")


@login_required
def edit_course(request, pk):
    template = "course/edit.html"
    course = get_object_or_404(course, pk=pk)
    form = CourseForm(request.GET or None, instance=course)
    context = {"form": form}
    return render(request, template, context)


@login_required
def update_course(request, pk):
    if request.method == "POST":
        course = get_object_or_404(course, pk=pk)
        form = CourseForm(request.POST or None, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "course Updated Successfully")
            return redirect("list_course")
        else:
            messages.error(request, "course Update Failed")
            return redirect("edit_course")
