from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            'first_name', 'last_name', 'age', 'blood_type',
            'admission_age', 'reason', 'status'
        ]
