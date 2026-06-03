from django.db import models
from core.models import BaseModel
from patients.models import Patient
from django.conf import settings

class TriageRecord(BaseModel):

    PRIORITY_LEVELS = (
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("CRITICAL", "Critical"),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    blood_pressure = models.CharField(max_length=20)
    temperature = models.FloatField()
    pulse_rate = models.IntegerField()
    oxygen_level = models.IntegerField()
    symptoms = models.TextField()

    priority_level = models.CharField(
        max_length=20,
        choices=PRIORITY_LEVELS,
        default="LOW"
    )

    triage_status = models.CharField(
        max_length=50,
        default="WAITING"
    )

    nurse = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="triage_entries"
    )

    def __str__(self):
        return f"{self.patient.full_name} - {self.priority_level}"