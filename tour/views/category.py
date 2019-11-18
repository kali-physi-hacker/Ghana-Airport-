from django.shortcuts import render 

from tour.models.category import Category


def list_categories(request):
    template = "category/list.html"
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, template, context)