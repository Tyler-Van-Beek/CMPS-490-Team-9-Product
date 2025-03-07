from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World! I'm at the home page.")

def about(request):
    return HttpResponse("This is the about page")
