from django import forms 
from events.models import Event, Registration

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

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['UserID', 'EventID']