"""
URL configuration for lagniappe_signup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views
from events.models import Users, Event, Category, Feedback, Registration

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage,name='home'),
    path('about/', views.about),
    path('signin/',views.signin,name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signup/SignUpForm', views.signupform, name="sign-up-form"),
    path('event/create', views.create_event, name="event-create"),
    path('event/list', views.list_event.as_view(), name="event-list"),
    path('registration/create', views.create_reg, name="registration-create"),
    path('registration/list', views.list_reg.as_view(), name="registration-list"),
    path('registration/RegistrationForm/', views.RegistrationForm, name="registration-form"),
    path('event/event-list/', views.eventForm, name="event-form"),
    path('map/', views.eventMap,name='map'),
    path('feedback/create', views.create_feedback,name='feedback-create'),
    path('feedback/list/', views.list_feedback.as_view(), name="feedback-list"),
]
