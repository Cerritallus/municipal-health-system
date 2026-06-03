from django.shortcuts import render
from triage.models import TriageRecord
from security.decorators import role_required

@role_required(["DOCTOR", "ADMIN"])
def doctor_dashboard(request):

    queue = TriageRecord.objects.all().order_by(
        "-priority_level",
        "created_at"
    )

    return render(request, "dashboard/doctor.html", {
        "queue": queue
    })


from django.shortcuts import redirect
from .models import DoctorAction

@role_required(["DOCTOR"])
def bulk_discharge(request):

    if request.method == "POST":

        ids = request.POST.getlist("patient_ids")

        for i in ids:
            DoctorAction.objects.filter(patient_id=i).update(
                discharged=True
            )

        return redirect("/dashboard/")