from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(max_length=10, null=True )
    email = models.EmailField(max_length=100, unique=True)
    contact = models.CharField(max_length=20, unique=True, null=True)
    
    
