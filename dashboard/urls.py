from django.urls import path
from .views import doctor_dashboard, bulk_discharge

urlpatterns = [
    path("", doctor_dashboard),
    path("bulk-discharge/", bulk_discharge),
]