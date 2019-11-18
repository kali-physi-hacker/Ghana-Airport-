from django.shortcuts import render

from tour.models.trip import Trip
from tour.forms.trip import TripForm

# Create your views here.
def home(request):
    template = "index.html"
    context = {}
    return render(request, template, context)


def list_trip(request):
    template = "trip/list.html"
    trips = Trip.objects.all()
    context = {"trips": trips}
    return render(request, template, context)


def add_trip(request):
    template = "trip/add.html"
    if request.method == "POST":
        form = TripForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home")