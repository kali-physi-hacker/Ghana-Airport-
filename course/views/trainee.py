from django.shortcuts import render, redirect
from django.contrib import messages

from django_countries.fields import countries

from course.models.trainee import Trainee

from course.forms.trainee import TraineeForm
from course.forms.trainee_course import TraineeCourseForm


def list_trainees(request):
    template = "trainee/list.html"
    trainees = Trainee.objects.all()
    context = {
        "trainees": trainees, "list_trainee_active": "active", "trainee_show": "show"
    }
    return render(request, template, context)


def add_trainee(request):
    template = "trainee/add.html"
    form = TraineeForm()
    context = {
        "form": form, "countries": countries, "add_trainee_active": "active", "trainee_show": "show"
    }
    return render(request, template, context)


def create_trainee(request):
    if request.method == "POST":
        form = TraineeForm(request.POST or None, request.FILES or None)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Trainee Created Successfully")
            return redirect("list_trainee")
        else:
            messages.error(request, "Trainee Creation Failed")
            return redirect("add_trainee")


def edit_trainee(request, pk):
    template = "trainee/edit.html"
    form = TraineeForm()
    context = {
        "form": form
    }
    return render(request, template, context)
