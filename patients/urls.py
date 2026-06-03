from django.urls import path
from . import views

urlpatterns = [
    path("", views.patient_list, name="patient_list"),
    path("create/", views.patient_create, name="patient_create"),
]