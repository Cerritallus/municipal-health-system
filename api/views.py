from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from patients.models import Patient
from triage.models import TriageRecord
from .serializers import PublicPatientSerializer, TriageRecordSerializer


# =========================================================
# PUBLIC HEALTH DASHBOARD API (MASKED)
# =========================================================

class PublicHealthStats(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        total_patients = Patient.objects.count()
        critical_cases = TriageRecord.objects.filter(priority_level="CRITICAL").count()

        data = {
            "total_patients": total_patients,
            "critical_cases": critical_cases,
            "message": "Individual patient data is HIPAA Restricted"
        }

        return Response(data)


# =========================================================
# PATIENT LIST API (MASKED)
# =========================================================

class PublicPatientAPI(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        patients = Patient.objects.all()[:50]
        serializer = PublicPatientSerializer(patients, many=True)

        return Response(serializer.data)


# =========================================================
# DOCTOR FULL API (AUTH REQUIRED)
# =========================================================

class DoctorTriageAPI(APIView):

    from .permissions import IsDoctorOrAdmin
    permission_classes = [IsDoctorOrAdmin]

    def get(self, request):

        if request.user.role not in ["DOCTOR", "ADMIN"]:
            return Response({"error": "Forbidden"}, status=403)

        records = TriageRecord.objects.all()
        serializer = TriageRecordSerializer(records, many=True)

        return Response(serializer.data)