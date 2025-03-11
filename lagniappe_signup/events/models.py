from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.
class User(AbstractUser):
    UserID = models.IntegerField(("userID"), primary_key=True, unique=True)
    Email = models.EmailField("email", unique=True)
    Password = models.CharField(_("password"), max_length=50)

class Category(models.Model):
    CategoryID = models.CharField(("categoryID"), primary_key= True, unique=True, max_length=50)
    Name = models.CharField(("name"), unique=True, max_length=200)

class Event(models.Model):
    EventID = models.IntegerField(("eventID"), primary_key=True, unique=True)
    OrganizerID = models.ForeignKey(User, on_delete=models.CASCADE)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    Title = models.CharField(("title"), max_length=100)
    Description = models.CharField(("description"), max_length=100)
    Location = models.CharField(("location"), max_length=100)
    DateTime = models.DateTimeField(("datetime"), null=True)
    EventStatus = models.BooleanField(("eventstatus"), default=True)

class Feedback(models.Model):
    EventID = models.IntegerField(("eventID"), primary_key=True, unique=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    EventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    Rating = models.IntegerField(("rating"), default=1, validators=[MaxValueValidator(5)])
    Comments = models.CharField(("comments"), max_length=500)
    Date = models.DateTimeField(("date"), auto_now_add=True)

class Registration(models.Model):
    RegistrationID = models.IntegerField(("registrationID"), primary_key=True, unique=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    EventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    RegistrationStatus = models.BooleanField(("registrationstatus"), default=True)
    RegistrationDate = models.DateTimeField(("registrationdate"), auto_now_add=True)