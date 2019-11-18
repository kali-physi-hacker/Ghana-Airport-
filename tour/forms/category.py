from django import forms 

from tour.models.category import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"