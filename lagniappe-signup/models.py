from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

class Event(models.Model):
    organizerID = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField()
    Location = models.CharField(max_length=50)
    EventStatus = models.CharField(max_length=50)

class Feedback(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.CharField(max_length=500)
    date = models.DateField()

class Registration(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    registrationStatus = models.CharField(max_length=50)
    registrationDate = models.DateField()

class Category(models.Model):
    name = models.CharField(max_length=50)