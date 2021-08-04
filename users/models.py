from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

from django.contrib import admin

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

admin.site.register(CustomUser)