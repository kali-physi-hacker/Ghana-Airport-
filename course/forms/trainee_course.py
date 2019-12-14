from django import forms 

from course.models.trainee_course import TraineeCourse


class TraineeCourseForm(forms.ModelForm):
    class Meta:
        model = TraineeCourse
        fields = "__all__"