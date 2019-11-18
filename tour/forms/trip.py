from django import forms 

from tour.models.trip import Trip 


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip 
        fields = "__all__"