from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from events.models import Users, Event, Category, Feedback, Registration
from .forms import EventForm, SignUpForm, FeedbackForm
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

        sign = authenticate(username=username, password=password)
        print("Authenticated user:", sign)
        print("Submitted username:", username)
        print("Submitted password:", password)

        
        if sign is not None:
            login(request, sign)
            return redirect('home')
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
    event = Event.objects.all()

    # Pass data to the template
    context = {
        'form': form,
        'Users': users,
        'Events': event,
    }

    return render(request, 'create_feedback.html', context)

def feedback_form(request):
    if request.method == "POST":
        user = request.POST.get('User')
        event = request.POST.get('Event')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        event = Event.objects.get(EventID=event)
        user = Users.objects.get(UserID=user)

        feedback = Feedback(UserID=user, EventID=event, Rating=rating, Comments=comments)
        feedback.save()
        
        return redirect("feedback-list")
    else:
        return HttpResponse("Only POST requests are allowed.", status=405)
    
class list_feedback(ListView):
    model = Feedback
    template_name = 'feedback_list.html'
    context_object_name = 'feedback'
    paginate = 20  

def detail_event(request, pk):
    try:
        event = Event.objects.get(EventID=pk)
    except Event.DoesNotExist:
        raise HttpResponse('Event Does Not Exist', status=404)
    
    return render(request, 'event_detail.html', context={'event': event})

def update_event(request, pk):
    event = Event.objects.get(EventID=pk)

    if request.method == "POST":
        # Create form or handle form submission logic here
        # If you're using a form, you can validate and save it like this:
        form = EventForm(request.POST, instance=event)
        
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('event-list'), event.EventID)
        else:
            print(form.errors)
    
    else:
        # If it's a GET request, prepopulate the form with event data
        form = EventForm(instance=event)

    # Fetch users and categories for context
    users = Users.objects.all()
    category = Category.objects.all()

    # Add the context for the template
    context = {
        'event': event,
        'form': form,
        'Users': users,
        'Category': category,
    }

    return render(request, 'event_update.html', context)

def detail_user(request, pk):
    try:
        user = Users.objects.get(UserID=pk)
    except Event.DoesNotExist:
        raise HttpResponse('User Does Not Exist', status=404)
    
    return render(request, 'user_detail.html', context={'User': user})

class list_users(ListView):
    model = Users
    template_name = 'user_list.html'
    context_object_name = 'User'
    paginate = 20  

def event_registrations(request,pk):
    try:
        event = Event.objects.get(EventID=pk)
        reg = Registration.objects.filter(EventID=event)
    except Event.DoesNotExist or Registration.DoesNotExist:
        raise HttpResponse('Event or Registration Does Not Exist', status=404)

    return render(request, 'event_registrations.html', context={'Registrations': reg})