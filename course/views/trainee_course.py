from django.shortcuts import render, redirect
from django.contrib import messages 

from course.models.trainee_course import TraineeCourse
from course.models.trainee import Trainee
from course.forms.trainee_course import TraineeCourseForm


def list_trainee_course(request):
    template = "trainee_course/list.html"
    trainee_courses = TraineeCourse.objects.all()
    context = {
        "trainee_courses": trainee_courses,
        "trainee_course_list_active": "active",
        "trainee_active": "active"
    }
    return render(request, template, context)


def add_trainee_course(request, input_data=None):
    template = "trainee_course/add.html"
    form = TraineeCourseForm()
    trainees = Trainee.objects.all()
    context = {
        "form": form,
        "input_data": input_data,
        "trainees": trainees,
        "trainee_show": "show",
        "add_trainee_course_active": "active",
        "trainee_active": "active"
    }
    return render(request, template, context)


def create_trainee_course(request):
    if request.method == "POST":
        form = TraineeCourseForm(request.POST or None)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.sucess(request, "Trainee Course Added Successfully")
            return redirect("list_trainee_course")
        else:
            messages.error(request, "Trainee Course Creation Failed")
            return add_trainee_course(request, form) # redirect("add_trainee_course")