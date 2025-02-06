from Event.models import EventModel
from django import forms

class EventForm(forms.ModelForm):
    class Meta:
        model=EventModel
        fields='__all__'