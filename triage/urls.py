from django.urls import path
from .views import triage_create

urlpatterns = [
    path("<uuid:patient_id>/", triage_create),
]