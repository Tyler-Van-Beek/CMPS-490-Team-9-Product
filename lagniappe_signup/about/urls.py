from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.about_page, name='about'),  # Route to the about page
]
