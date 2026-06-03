from django.db import models
from core.models import BaseModel
from django.conf import settings

class Patient(BaseModel):

    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    emergency_contact = models.CharField(max_length=20)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patients_created"
    )

    def __str__(self):
        return self.full_name