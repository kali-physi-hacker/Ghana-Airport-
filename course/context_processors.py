from django.utils import timezone 
from django.contrib.auth.decorators import login_required

from course.models.notification import Notification
from course.models.course import Course

# @login_required
def return_next_trips():
    courses = Course.objects.filter(start_date__gte=timezone.now().date())
    return courses 


def show_notifications(request):
    courses = return_next_trips()
    for course in courses:
        title = course.name 
        message = course.description[:20] + "..."
        datetime = timezone.now()
        notifications = Notification.objects.all()
        for notification in notifications:
            if notification.title != title:
                Notification.objects.create(
                    title=title,
                    message=message,
                    datetime=datetime
                )

    notifications = Notification.objects.all()
    context = {'notifications': notifications}
    return context 


@login_required
def read_notification(request, pk):
    if request.method == "POST":
        notification = Notification.objects.get(pk=pk)
        notification.read = True 
        notification.save()
    else:
        import pdb; pdb.set_trace()