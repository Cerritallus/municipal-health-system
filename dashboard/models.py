from django.db import models
from core.models import BaseModel
from patients.models import Patient
from django.conf import settings

class DoctorAction(BaseModel):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    diagnosis = models.TextField()
    treatment = models.TextField()

    admitted = models.BooleanField(default=False)
    discharged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.full_name} - Action"