from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from tour.models.category import Category
from tour.forms.category import CategoryForm


def list_categories(request):
    template = "category/list.html"
    categories = Category.objects.all()
    context = {"categories": categories, "list_category_active": "active", "category_show": "show",
               "category_active": "active"}
    return render(request, template, context)


def add_category(request):
    template = "category/add.html"
    form = CategoryForm()
    context = {"form": form, "add_category_active": "active", "category_show": "show", "category_active": "active"}
    return render(request, template, context)


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Created Successfully")
            return redirect("list_categories")
        else:
            messages.error(request, "Category Creation Failed!")
            return redirect("add_category")


def edit_category(request, pk):
    template = "category/edit.html"
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.GET or None, instance=category)
    context = {"form": form}
    return render(request, template, context)


def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST or None, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Update Successfully")
            return redirect("list_categories")
        else:
            messages.error(request, "Category Update Failed!")
            return redirect("edit_category")
