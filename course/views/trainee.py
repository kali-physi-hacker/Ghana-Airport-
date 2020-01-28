from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from django_countries.fields import countries

from course.models.trainee import Trainee

from course.forms.trainee import TraineeForm
from course.forms.trainee_course import TraineeCourseForm


@login_required
def list_trainees(request):
    template = "trainee/list.html"
    trainees = Trainee.objects.all()
    context = {
        "trainees": trainees, "list_trainee_active": "active", "trainee_show": "show"
    }
    return render(request, template, context)


@login_required 
def detail_trainee(request, pk):
    if request.user.is_superuser:
        template = "trainee/detail.html"
        trainee = get_object_or_404(Trainee, pk=pk)
        context = {"trainee": trainee}
        return render(request, template, context)
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")

@login_required
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


@login_required
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


@login_required
def edit_trainee(request, pk):
    if request.user.is_superuser:
        template = "trainee/edit.html"
        trainee = get_object_or_404(Trainee, pk=pk)
        form = TraineeForm(request.GET or None, instance=trainee)
        country_edit_code = trainee.country.code 
        context = {
            "form": form, "countries": countries, "country_edit_code": country_edit_code, "sex": trainee.sex, "selected_status": trainee.status, "pk": pk
        }
        return render(request, template, context)
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")


@login_required
def update_trainee(request, pk):
    if request.user.is_superuser:
        if request.method == "POST":
            trainee = get_object_or_404(Trainee, pk=pk)
            form = TraineeForm(request.POST or None, instance=trainee)
            # import pdb; pdb.set_trace()
            if form.is_valid():
                form.save()
                messages.success(request, "Trainee Updated Successfully")
                return redirect("list_trainee")
            else:
                messages.error(request, "Trainee Update Failed")
                return redirect("edit_trainee", pk=pk)
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")


@login_required
def delete_trainee(request, pk):
    if request.user.is_superuser:
    # if request.method == "POST":
        trainee = get_object_or_404(Trainee, pk=pk)
        trainee.delete()
        messages.success(request, "Trainee Deleted Successfully")
        return redirect("list_trainee")
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")

