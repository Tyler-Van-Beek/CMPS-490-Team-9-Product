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
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate


def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        sign = authenticate(request, username=username, password=password)
        print("Authenticated user:", sign)
        print("Submitted username:", username)
        print("Submitted password:", password)

        
        if sign is not None:
            login(request, sign)
            return redirect('home')
    return render(request,'signin.html')

def eventMap(request):
    return render(request,'eventMap.html')

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')  
    else:
        form = EventForm(request)

    # Fetch Users and Events for the context
    users = Users.objects.all()
    category = Category.objects.all()

    # Pass data to the template
    context = {
        'form': form,
        'Users': users,
        'Category': category,
    }

    return render(request, 'create_event.html', context)

def eventForm(request):
    if request.method == 'POST':
        organizer = request.POST.get('Organizer')
        category = request.POST.get('Category')
        title = request.POST.get('Title')
        description = request.POST.get('Description')
        location = request.POST.get('Location')
        dateTime = request.POST.get('DateTime')

        organizer = Users.objects.get(UserID=organizer)
        category = Category.objects.get(Name=category)

        event = Event(OrganizerID=organizer, CategoryID=category, Title=title, Description=description, Location=location, DateTime=dateTime)
        event.save()

        return redirect("event-list")
    else:
        return HttpResponse("Only POST requests are allowed.", status=405)

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
