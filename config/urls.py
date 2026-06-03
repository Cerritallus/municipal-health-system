from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("You're not supposed to be here.")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    path("patients/", include("patients.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("api/", include("api.urls")),

    path('', home),
]