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
    path('event/create', views.create_event.as_view(), name="event-create"),
    path('event/list', views.list_event.as_view(), name="event-list"),
    path('registration/create', views.create_reg.as_view(), name="registration-create")
]
