from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('DOCTOR', 'Doctor'),
        ('NURSE', 'Nurse'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='NURSE'
    )

    def __str__(self):
        return f"{self.username} - {self.role}"