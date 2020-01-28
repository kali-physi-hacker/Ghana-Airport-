from django.utils import timezone 
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

    # Delete Notification Entries 
    Notification.objects.all().delete()
    
    courses = return_next_trips()
    notify_courses = []
    for course in courses:
        if course.notify() == 1:
            notify_courses.append(course)
    for course in notify_courses:
    # if course.notify() == 1:
        print('Worked')
        title = course.name
        try:
            message = course.description[:20] + "..."
        except TypeError:
            message = "No Descriptions"
        datetime = timezone.now()

        Notification.objects.create(
            title=title,
            message=message,
        )

    # for course in courses:
    #     title = course.name 
    #     try:
    #         message = course.description[:20] + "..."
    #     except TypeError:
    #         message = "No Descriptions"
    #     datetime = timezone.now()
    #     notifications = Notification.objects.all()
    #     for notification in notifications:
    #         if notification.title != title:
    #             Notification.objects.create(
    #                 title=title,
    #                 message=message,
    #                 datetime=datetime
    #             )

    notifications = Notification.objects.all()
    # import pdb; pdb.set_trace()
    context = {'notifications': notifications}
    return context 


# @login_required
def pie_chart(request):
    trainees = Trainee.objects.all()
    employees = Employee.objects.all().count()
    trainees_done = trainees.filter(status='D').count()
    trainees_pending = trainees.filter(status='P').count()
    total_entities = employees + trainees_done + trainees_pending

    # import pdb; pdb.set_trace()
    trainees_done_pie = (trainees_done/total_entities)*100
    trainees_pending_pie = (trainees_pending/total_entities)*100
    employees_pie = (employees/total_entities)*100

    context = {
        "employees": employees_pie, "trainees_done": trainees_done_pie, "trainees_pending": trainees_pending_pie
    }
    return context 


def area_chart(request):
    trainees = Trainee.objects.all()
    courses = Course.objects.all()
    months = [i+1 for i in range(12)]
    month_count = []
    for i in months:
        month_count.append(courses.filter(start_date__month=str(i)))
    context = {}
    month_names = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
    for n, i in enumerate(month_names):
        context[i] = month_count[n].count()
        print(context[i])
    # import pdb; pdb.set_trace()
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
    # import pdb; pdb.set_trace()
    return context


@login_required
def read_notification(request, pk):
    if request.method == "POST":
        notification = Notification.objects.get(pk=pk)
        notification.read = True 
        notification.save()
    else:
        import pdb; pdb.set_trace()