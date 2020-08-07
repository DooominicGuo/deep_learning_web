from django.db import models
from django import forms
# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    creation_time = models.DateTimeField()
class Choice(models.Model):
    firstChoice = models.CharField(max_length = 10)
    secondChoice = models.CharField(max_length = 10)
    thirdChoice = models.CharField(max_length = 10)
    created_by = models.CharField(max_length = 100)
    creation_time = models.DateTimeField()
    postID = models.CharField(max_length = 20)

    
