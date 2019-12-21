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


def add_trainee(request, input_data=None):
    template = "trainee/add.html"
    form = TraineeForm()
    context = {
        "form": form, "input_data":input_data, "countries": countries, "add_trainee_active": "active", "trainee_show": "show"
    }

    if input_data is not None:
        input_country = input_data.data.get("country")
        # import pdb; pdb.set_trace()
        for country in countries:
            if country[0] == input_country:
                country_input_name = country[1]
                country_input_code = country[0]
                context['country_input_name'] = country_input_name
                context['country_input_code'] = country_input_code

        input_status = input_data.data.get("status")
        status_data = {"D": "Done", "P": "Pending", "-------- Select Status -----------": None}
        context['status_code'] = input_status
        # import pdb; pdb.set_trace()
        context['status_name'] = status_data[input_status]

        input_sex = input_data.data.get("sex")
        context['sex'] = input_sex
        # import pdb; pdb.set_trace()
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
            return add_trainee(request, form)  # redirect("add_trainee")


def edit_trainee(request, pk):
    template = "trainee/edit.html"
    form = TraineeForm()
    context = {
        "form": form
    }
    return render(request, template, context)
