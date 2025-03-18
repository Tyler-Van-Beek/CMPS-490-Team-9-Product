from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse

def homepage(request):

    return render(request,'home.html')


def about_page(request):
    """
    View function for the About Us page.
    """
    return render(request, 'about/about.html')