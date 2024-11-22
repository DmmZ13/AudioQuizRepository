from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(AbstractUser):
    tipo = models.BooleanField()  # True ou False
    password = models.CharField(max_length=128, default=make_password("default_password"))  # Valor padrão
    username = models.CharField(max_length=150, unique=True, default="default_username")
    def __str__(self):
        return self.username  
    