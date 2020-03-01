from django.utils import timezone
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from course.models.notification import Notification
from course.models.course import Course

from course.models.employee import Employee
from course.models.trainee import Trainee


# @login_required
def return_next_trips():
    courses = Course.objects.filter(start_date__gte=timezone.now().date())
    return courses


def get_ongoing_courses():
    courses = Course.objects.filter(start_date__lte=timezone.now()).filter(end_date__gte=timezone.now())
    return courses


def show_notifications(request):
    # Notification.objects.all().delete()

    courses = return_next_trips()
    notify_courses = []
    for course in courses:
        if course.notify() == 1:
            notify_courses.append(course)
    for course in notify_courses:
        # print('Worked')
        title = course.name
        try:
            message = course.description + "..."
        except TypeError:
            message = "No Descriptions"
        datetime = timezone.now()

        try:
            Notification.objects.create(
                unique_id=course.id,
                title=title,
                message=message,
            )
        except IntegrityError:
            # print("Notification already exist")
            import pdb; pdb.set_trace() 

    notifications = Notification.objects.all().filter(read=False)
    context = {'notifications': notifications}
    return context


# @login_required
def pie_chart(request):
    trainees = Trainee.objects.all()
    employees = Employee.objects.all().count()
    trainees_done = trainees.filter(status='D').count()
    trainees_pending = trainees.filter(status='P').count()
    total_entities = employees + trainees_done + trainees_pending

    trainees_done_pie = 0
    try:
        trainees_done_pie = (trainees_done / total_entities) * 100
    except ZeroDivisionError:
        trainee_done_pie = 0

    try:
        trainees_pending_pie = (trainees_pending / total_entities) * 100
    except ZeroDivisionError:
        trainees_pending_pie = 0

    try:
        employees_pie = (employees / total_entities) * 100
    except ZeroDivisionError:
        employees_pie = 0

    context = {
        "employees": employees_pie, "trainees_done": trainees_done_pie, "trainees_pending": trainees_pending_pie
    }
    return context


def area_chart(request):
    trainees = Trainee.objects.all()
    courses = Course.objects.all()
    months = [i + 1 for i in range(12)]
    month_count = []
    for i in months:
        month_count.append(courses.filter(start_date__month=str(i)))
    context = {}
    month_names = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
    for n, i in enumerate(month_names):
        context[i] = month_count[n].count()
    return context


def ongoing_courses(request):
    colors = [
        '#4e73df', '#6610f2', '#6f42c1', '#e83e8c', "#e74a3b", "#fd7e14", "#f6c23e", "#1cc88a", "#20c9a6", "#36b9cc",
    ]
    courses = get_ongoing_courses()
    courses_lst = []
    for i, course in enumerate(courses):
        try:
            courses_lst.append([colors[i], course])
        except IndexError:
            i = 0
    context = {"ongoing_courses": courses_lst}
    return context


@login_required
def read_notification(request, pk):
    if request.method == "POST":
        notification = Notification.objects.get(pk=pk)
        notification.read = True
        notification.save()
    else:
        import pdb;
        pdb.set_trace()
