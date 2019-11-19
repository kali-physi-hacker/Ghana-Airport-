from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from tour.models.trip import Trip
from tour.models.employee import Employee
from tour.forms.trip import TripForm


# Create your views here.
def home(request):
    template = "index.html"
    context = {}
    return render(request, template, context)


def list_trip(request):
    template = "trip/list.html"
    trips = Trip.objects.all()
    context = {"trips": trips, "list_trip_active": "active", "trip_show": "show", "trip_active": "active"}
    return render(request, template, context)


def add_trip(request):
    template = "trip/add.html"
    form = TripForm()
    employees = Employee.objects.all()
    context = {"form": form, "employees": employees, "add_trip_active": "active", "trip_show": "show", "trip_active": "active"}
    return render(request, template, context)


def create_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST or None)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Trip Added Successfully")
            return redirect("list_trip")
        else:
            messages.error(request, "Trip Creation Failed")
            return redirect("add_trip")


def edit_trip(request, pk):
    template = "trip/edit.html"
    trip = get_object_or_404(Trip, pk=pk)
    form = TripForm(request.GET or None, instance=trip)
    context = {"form": form}
    return render(request, template, context)


def update_trip(request, pk):
    if request.method == "POST":
        trip = get_object_or_404(Trip, pk=pk)
        form = TripForm(request.POST or None, instance=trip)
        if form.is_valid():
            form.save()
            messages.success(request, "Trip Updated Successfully")
            return redirect("list_trip")
        else:
            messages.error(request, "Trip Update Failed")
            return redirect("edit_trip")
