from django.db import models
from django.utils import timezone

class Client(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    dateOfBirth = models.DateField(default=timezone.now)
    email = models.EmailField(max_length=191, unique=True)
    phone = models.CharField(max_length=15)
