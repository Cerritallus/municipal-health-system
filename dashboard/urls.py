from django.urls import path
from .views import doctor_dashboard, bulk_discharge, patient_detail

urlpatterns = [
    path("", doctor_dashboard),
    path("bulk-discharge/", bulk_discharge),
    path("patient/<uuid:patient_id>/", patient_detail),
]