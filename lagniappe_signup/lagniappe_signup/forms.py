from django import forms 
from events.models import Event, Registration, Users, Feedback

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

class SignUpForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'UserID',
            'EventID',
            'Rating',
            'Comments',
        ]