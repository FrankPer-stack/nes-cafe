from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Campos adicionales
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    # Campos para el sistema de café
    favorite_coffee = models.CharField(max_length=100, blank=True, null=True)
    coffee_preferences = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.email
