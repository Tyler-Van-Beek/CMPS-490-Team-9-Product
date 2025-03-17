from django import forms 
from events.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = [
            'OrganizerID',
            'CategoryID',
            'Title',
            'Description',
            'Location',
            'DateTime',
            'EventStatus',
        ]