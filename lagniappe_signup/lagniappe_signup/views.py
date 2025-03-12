from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse

def homepage(request):

    return render(request,'home.html')


def about(request):
    return HttpResponse("This is the about page")
