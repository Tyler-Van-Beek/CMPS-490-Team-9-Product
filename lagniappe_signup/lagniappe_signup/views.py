from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from events.models import Users, Event, Category, Feedback, Registration
from .forms import EventForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

def homepage(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse("This is the about page")

def signin(request):
    return render(request,'signin.html')
class create_event(CreateView):
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
    template_name = 'create_view.html'
    success_url = reverse_lazy('event/list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch Users and Categories and add them to the context
        context['Users'] = Users.objects.all()
        context['Category'] = Category.objects.all()
        
        return context

class list_event(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    paginate = 20

class create_reg(CreateView):
    model = Registration
    fields = [
            'UserID',
            'EventID',
        ]
    template_name = 'create_registration.html'
    success_url = reverse_lazy('')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch Users and Categories and add them to the context
        context['Users'] = Users.objects.all()
        context['Events'] = Event.objects.all()
        
        return context
    
# (creating list and create views for event, getting HTTP error for both of them)
