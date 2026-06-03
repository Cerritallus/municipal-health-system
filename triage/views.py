from django.shortcuts import render, redirect
from patients.models import Patient
from .models import TriageRecord
from security.decorators import role_required

@role_required(["NURSE"])
def triage_create(request, patient_id):

    patient = Patient.objects.get(id=patient_id)

    if request.method == "POST":

        temp = float(request.POST["temperature"])
        oxygen = int(request.POST["oxygen_level"])

        # AUTO PRIORITY ENGINE
        if temp > 39 or oxygen < 92:
            priority = "CRITICAL"
        elif temp > 38:
            priority = "HIGH"
        else:
            priority = "MEDIUM"

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