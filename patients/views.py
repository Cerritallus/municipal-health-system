from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from security.decorators import role_required
from security.audit import log_event

@role_required(["NURSE", "ADMIN"])
def patient_list(request):

    patients = Patient.objects.all()

    context = {
        "patients": patients,
        "pending_count": patients.filter(triagerecord__isnull=True).count(),
        "completed_count": patients.filter(triagerecord__isnull=False).count(),
    }

    return render(request, "patients/list.html", context)


@role_required(["NURSE", "ADMIN"])
def patient_create(request):

    if request.method == "POST":

        Patient.objects.create(
            full_name=request.POST["full_name"],
            birth_date=request.POST["birth_date"],
            address=request.POST["address"],
            contact_number=request.POST["contact_number"],
            emergency_contact=request.POST["emergency_contact"],
            created_by=request.user
        )

        log_event(
            request.user.username,
            "CREATE_PATIENT",
            request.POST["full_name"]
        )

        return redirect("/patients/")

    return render(request, "patients/create.html")