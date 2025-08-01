# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username