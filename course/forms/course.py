from django import forms 

from course.models.course import Course 


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course 
        fields = "__all__"