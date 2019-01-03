from django.db import models
from multiselectfield import  MultiSelectField
from .porter import *
import datetime
# Create your models here.


class RegistrationData(models.Model):
    username = models.TextField(max_length=20)
    email = models.EmailField(max_length=30)
    upassword = models.TextField(max_length=100)
    # dob =models.DateField(null=True, blank=True)
    location = MultiSelectField(choices=LOCATION_CHOICES ,max_length=20 , max_choices=3 )
    gender = models.CharField(max_length=20 , choices=GENDER_CHOICES)


