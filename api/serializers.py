from rest_framework import serializers
from patients.models import Patient
from triage.models import TriageRecord


# =========================================================
# PUBLIC SERIALIZER (MASKED OUTPUT)
# =========================================================

class PublicPatientSerializer(serializers.ModelSerializer):

    patient_name = serializers.SerializerMethodField()
    symptoms = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'patient_name', 'symptoms']

    def get_patient_name(self, obj):
        return "HIPAA Restricted"

    def get_symptoms(self, obj):
        return "HIPAA Restricted"


# =========================================================
# FULL TRIAGE SERIALIZER (AUTH ONLY)
# =========================================================

class TriageRecordSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(source="patient.full_name")

    class Meta:
        model = TriageRecord
        fields = [
            'id',
            'patient_name',
            'blood_pressure',
            'temperature',
            'pulse_rate',
            'oxygen_level',
            'symptoms',
            'priority_level',
            'triage_status',
        ]