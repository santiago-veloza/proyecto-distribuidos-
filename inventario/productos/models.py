from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('jefe', 'Jefe'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='admin')

    def __str__(self):
        return f"{self.username} - {self.rol}"

