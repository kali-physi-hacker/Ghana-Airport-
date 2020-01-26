from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django_countries.fields import countries

from course.models.course import Course
from course.models.trainee import Trainee
from course.models.employee import Employee
from course.models.category import Category

from course.models.notification import Notification

from course.forms.course import CourseForm


# @login_required
def return_next_trips():
    courses = Course.objects.filter(start_date__gte=timezone.now().date())
    return courses 


# Create your views here.
@login_required
def home(request):
    template = "index.html"
    total_employees = len(Employee.objects.all())
    total_courses = len(Course.objects.all())
    total_trainees = len(Trainee.objects.all())
    total_categories = len(Category.objects.all())

    context = {
        "total_employees": total_employees,
        "total_trainees": total_trainees,
        "total_courses": total_courses,
        "total_categories": total_categories
    }

    # pending_trainees = Trainee.objects.filter(status='P').filter(start_date)
    """for trainee in pending_trainees:
        if trainee"""

    return render(request, template, context)


@login_required
def list_course(request):
    template = "course/list.html"
    courses = Course.objects.all()
    context = {"courses": courses, "list_course_active": "active", "course_show": "show", "course_active": "active"}
    return render(request, template, context)


@login_required
def add_course(request, input_data=None):
    template = "course/add.html"
    form = CourseForm()
    employees = Employee.objects.all()
    context = {"form": form, "input_data":input_data, "employees": employees, "add_course_active": "active", "course_show": "show", "course_active": "active", "countries":countries}
    return render(request, template, context)


@login_required
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST or None)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Course Added Successfully")
            return redirect("list_course")
        else:
            # import pdb; pdb.set_trace()
            messages.error(request, "Course Creation Failed")
            return add_course(request, form) # redirect("add_course_args", input_data=2)


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
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(request.POST or None, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "course Updated Successfully")
            return redirect("list_course")
        else:
            messages.error(request, "course Update Failed")
            return redirect("edit_course")


@login_required
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, "Course Deleted Successfully")
    return redirect("list_course")