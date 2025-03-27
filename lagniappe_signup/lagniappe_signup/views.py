from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from events.models import Users, Event, Category, Feedback, Registration
from .forms import EventForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

def homepage(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse("This is the about page")

def signin(request):
    return render(request,'signin.html')

def eventMap(request):
    return render(request,'eventMap.html')
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
    
    template_name = 'create_event.html'
    success_url = reverse_lazy('lagniappe_signup:event-list')

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

def create_reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration-list')  
    else:
        form = RegistrationForm(request)

    # Fetch Users and Events for the context
    users = Users.objects.all()
    events = Event.objects.all()

    # Pass data to the template
    context = {
        'form': form,
        'Users': users,
        'Events': events,
    }

    return render(request, 'create_registration.html', context)
    
class list_reg(ListView):
    model = Registration
    template_name = 'registration_list.html'
    context_object_name = 'registrations'
    paginate = 20  
@csrf_exempt
def RegistrationForm(request):
    if request.method == 'POST':
        eventID = request.POST.get('Event')
        userID = request.POST.get('User')

        event = Event.objects.get(EventID=eventID)
        user = Users.objects.get(UserID=userID)
        
        registration = Registration(UserID=user, EventID=event)
        registration.save()

        return redirect("registration-list")
    else:
        return HttpResponse("Only POST requests are allowed.", status=405)

# (creating list and create views for event, getting HTTP error for both of them)
