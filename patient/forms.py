from django.forms import ModelForm, Textarea, TextInput, Select
from patient.models import PatientVitals, Vitals

class PatientVitalsForm(ModelForm):
    vitals = Vitals.objects.filter(active__exact = 1)
    vital_fields = {}
    for vital in vitals:
        vital_fields[vital.id] = vital.name
    class Meta:
        model = PatientVitals
        fields = ['measures']
        widgets = {
            'measures':TextInput(attrs={'class':'form-control'})           
        }        
    
