from django.urls import path
from .views import PublicHealthStats, PublicPatientAPI, DoctorTriageAPI
from .jwt_views import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path("public/stats/", PublicHealthStats.as_view()),
    path("public/patients/", PublicPatientAPI.as_view()),
    path("doctor/triage/", DoctorTriageAPI.as_view()),

    # JWT
    path("token/", CustomTokenObtainPairView.as_view()),
    path("token/refresh/", CustomTokenRefreshView.as_view()),
]