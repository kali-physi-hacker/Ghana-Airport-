from django import forms

from course.models.trainee import Trainee


class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee 
        fields = "__all__"

        error_messages = {
            "mobile_number": {
                "invalid": "Please enter a valid telephone number"
            }
        }