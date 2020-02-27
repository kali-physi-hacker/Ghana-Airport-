from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import PermissionDenied

from django_countries.fields import countries

from course.models.course import Course
from course.models.trainee import Trainee
from course.models.employee import Employee
from course.models.category import Category
from course.models.notification import Notification

from course.models.notification import Notification

from course.forms.course import CourseForm


# Create your views here.
@login_required
def home(request):
    template = "index.html"
    # import pdb; pdb.set_trace()
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
def read_notification(request, notification_id):
    notification = Notification.objects.get(pk=notification_id)
    notification.read = True
    notification.save()
    previous_url = request.META.get("HTTP_REFERER")
    return redirect(previous_url)
    # import pdb; pdb.set_trace()


@login_required
def list_course(request):
    template = "course/list.html"
    courses = Course.objects.all().order_by('-pk')
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
def add_by_rank(request):
    rank_name = request.GET.get("rank")
    rank = Category.objects.filter(name=rank_name)[0].pk
    # import pdb; pdb.set_trace()
    template = "course/add_by_rank.html"
    form = CourseForm()
    employees = Employee.objects.all()
    ranked_employees = Employee.objects.filter(category=rank)
    context = {
        "form": form, "employees": employees, "add_course_active": "active", "course_show": "show", 
        "course_active": "active", "countries":countries, "ranked_employees": ranked_employees, "rank": rank
    }
    return render(request, template, context)


@login_required
def create_by_rank(request, rank):
    if request.method == "POST":
        employee_list = [i.pk for i in Employee.objects.filter(category=rank)]
        request.POST = request.POST.copy()
        request.POST.setlist("employees", employee_list)
        form = CourseForm(request.POST or None)
        # import pdb; pdb.set_trace()
        print("A print statement")
        if form.is_valid():
            form.save()
            messages.success(request, "Course Added Successfully")
            return redirect("list_course")
        else:
            messages.error(request, "Course Creation Failed")
            return add_course(request, form)

@login_required
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST or None)
        request.POST = request.POST.copy()
        if form.is_valid():
            form.save()
            messages.success(request, "Course Added Successfully")
            return redirect("list_course")
        else:

            messages.error(request, "Course Creation Failed")
            return add_course(request, form) # redirect("add_course_args", input_data=2)


@login_required
def edit_course(request, pk):
    if request.user.is_superuser:
        template = "course/edit.html"
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(request.GET or None, instance=course)
        country_edit_code = course.country.code 
        employees = Employee.objects.all()
        selected_employees = course.employees.all()
        unselected_employees = [employee for employee in employees if employee not in selected_employees]
        context = {"form": form, "country_edit_code": country_edit_code, "pk": pk, "countries": countries, "employees": employees, "selected_employees": selected_employees, "unselected_employees": unselected_employees}
        return render(request, template, context)
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")
        


@login_required
def update_course(request, pk):
    if request.user.is_superuser:
        if request.method == "POST":
            course = get_object_or_404(Course, pk=pk)
            form = CourseForm(request.POST or None, instance=course)
            if form.is_valid():
                form.save()
                messages.success(request, "Course Updated Successfully")
                return redirect("list_course")
            else:
                messages.error(request, "Course Update Failed")
                return redirect("edit_course")
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")


@login_required
def delete_course(request, pk):
    if request.user.is_superuser:
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        messages.success(request, "Course Deleted Successfully")
        return redirect("list_course")
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")