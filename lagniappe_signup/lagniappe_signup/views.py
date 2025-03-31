from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from events.models import Users, Event, Category, Feedback, Registration
from .forms import EventForm, SignUpForm, FeedbackForm
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
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration-list')  
    else:
        form = SignUpForm(request)

    return render(request, 'create_user.html')

def signupform(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        Username = request.POST.get('username')
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        user = Users(first_name=firstname, last_name=lastname, username=Username, email=Email, password=Password)
        user.save()

        return redirect("home")
    else:
        return HttpResponse("Only POST requests are allowed.", status=405)

def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration-list')  
    else:
        form = FeedbackForm(request)

    # Fetch Users and Events for the context
    users = Users.objects.all()
    events = Event.objects.all()

    # Pass data to the template
    context = {
        'form': form,
        'Users': users,
        'Events': events,
    }

    return render(request, 'create_feedback.html', context)

# (creating list and create views for event, getting HTTP error for both of them)
