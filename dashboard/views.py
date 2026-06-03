from django.shortcuts import render
from triage.models import TriageRecord
from security.decorators import role_required

@role_required(["DOCTOR", "ADMIN"])
def doctor_dashboard(request):

    queue = TriageRecord.objects.exclude(
        triage_status="DISCHARGED"
    )

    context = {
        "queue": queue,
        "total_patients": queue.count(),
        "critical_count": queue.filter(priority_level="CRITICAL").count(),
        "high_count": queue.filter(priority_level="HIGH").count(),
        "discharged_count": queue.filter(triage_status="DISCHARGED").count(),
    }

    return render(request, "dashboard/doctor.html", context)


from django.shortcuts import redirect
from triage.models import TriageRecord

@role_required(["DOCTOR", "ADMIN"])
def bulk_discharge(request):

    if request.method == "POST":

        patient_ids = request.POST.getlist("patient_ids")

        records = TriageRecord.objects.filter(
            patient_id__in=patient_ids
        )

        for record in records:
            record.triage_status = "DISCHARGED"
            record.save()

    return redirect("/dashboard/")
    

from django.shortcuts import get_object_or_404
from triage.models import TriageRecord

def patient_detail(request, patient_id):

    record = get_object_or_404(TriageRecord, patient_id=patient_id)

    return render(request, "dashboard/patient_detail.html", {
        "record": record
    })