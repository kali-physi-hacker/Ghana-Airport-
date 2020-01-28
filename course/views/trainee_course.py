from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.core.exceptions import PermissionDenied

from course.models.trainee_course import TraineeCourse
from course.models.trainee import Trainee
from course.forms.trainee_course import TraineeCourseForm


def list_trainee_course(request):
    template = "trainee_course/list.html"
    trainee_courses = TraineeCourse.objects.all()
    context = {
        "trainee_courses": trainee_courses,
        "trainee_show": "show",
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
            messages.success(request, "Trainee Course Added Successfully")
            return redirect("list_trainee_course")
        else:
            messages.error(request, "Trainee Course Creation Failed")
            return add_trainee_course(request, form) 


def edit_trainee_course(request, pk):
    if request.user.is_superuser:
        template = "trainee_course/edit.html"
        trainee_course = get_object_or_404(TraineeCourse, pk=pk)
        trainees = Trainee.objects.all()
        selected_trainees = trainee_course.trainee.all()
        unselected_trainees = [trainee for trainee in trainees if trainee not in selected_trainees]
        # import pdb; pdb.set_trace()
        form = TraineeCourseForm(request.GET or None, instance=trainee_course)
        context = {"trainee_course": trainee_course, "form": form, 'pk': pk, "selected_trainees": selected_trainees, "unselected_trainees": unselected_trainees}
        return render(request, template, context)
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")


def update_trainee_course(request, pk):
    # import pdb; pdb.set_trace()
    if request.user.is_superuser:
        if request.method == "POST":
            trainee_course = get_object_or_404(TraineeCourse, pk=pk)
            form = TraineeCourseForm(request.POST or None, instance=trainee_course)
            # import pdb; pdb.set_trace()
            if form.is_valid():
                form.save()
                messages.success(request, "Trainee Updated Successfully")
                return redirect("list_trainee_course")
            else:
                messages.error(request, "Trainee Update Failed!!!")
                return redirect("edit_trainee_course")
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")


def delete_trainee_course(request, pk):
    if request.user.is_superuser:
        trainee_course = get_object_or_404(TraineeCourse, pk=pk)
        trainee_course.delete()
        messages.success(request, "Trainee Course Deleted Successfully")
        return redirect("list_trainee_course")