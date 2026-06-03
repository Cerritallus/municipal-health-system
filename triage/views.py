from django.shortcuts import render, redirect
from patients.models import Patient
from .models import TriageRecord
from security.decorators import role_required
from .services import calculate_priority

@role_required(["NURSE"])
def triage_create(request, patient_id):

    patient = Patient.objects.get(id=patient_id)

    if request.method == "POST":

        temp = float(request.POST["temperature"])
        oxygen = int(request.POST["oxygen_level"])

        priority = calculate_priority(
            temperature=float(request.POST.get("temperature")),
            oxygen_level=float(request.POST.get("oxygen_level")),
            pulse_rate=int(request.POST.get("pulse_rate")),
            symptoms=request.POST.get("symptoms")
        )

        TriageRecord.objects.create(
            patient=patient,
            blood_pressure=request.POST["blood_pressure"],
            temperature=temp,
            pulse_rate=request.POST["pulse_rate"],
            oxygen_level=oxygen,
            symptoms=request.POST["symptoms"],
            priority_level=priority,
            nurse=request.user
        )

        return redirect("/patients/")

    return render(request, "triage/create.html", {
        "patient": patient
    })