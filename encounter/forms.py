from django.forms import ModelForm, Textarea, TextInput, Select
from encounter.models import PatientVitals, Vitals, EncounterPatientHistory, EncounterPatientExamination, EncounterDiagnosis 

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


class PatientEncounterHistoryForm(ModelForm):
    class Meta:
        model = EncounterPatientHistory
        fields = ['history']
        widgets = {
            'history':Textarea(
                attrs={'cols':4, 'rows':5, 'class':"form-control"}
            ),
        }

class PatientEncounterExamForm(ModelForm):
    class Meta:
        model = EncounterPatientExamination
        fields = ['examination', 'notes']
        widgets = {
            'examination':Textarea(
                attrs={'cols':4, 'rows':5, 'class':"form-control"}
            ),
            'notes':Textarea(
                attrs={'cols':4, 'rows':5, 'class':"form-control"}
            ),
        }

class EncounterDiagnosisForm(ModelForm):
    class Meta:
        model = EncounterDiagnosis
        fields = ['diagnosis', 'notes']
        widgets = {
            'diagnosis':Textarea(
                attrs={'cols':4, 'rows':5, 'class':'form-control'}
            ),
            'notes':Textarea(
                attrs={'cols':4, 'rows':5, 'class':'form-control'}
            )
        }
