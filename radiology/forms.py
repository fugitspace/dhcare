from django.forms import ModelForm, Textarea, TextInput, Select
from radiology.models import PatientRadioRequest, PatientRadioReport

class PatientRadioRequestForm(ModelForm):    
    class Meta:
        model = PatientRadioRequest
        fields = ['clinical_summary', 'request_notes']
        widgets = {
            'clinical_summary':Textarea(
                attrs={'cols':4, 'rows':5, 'class':"form-control"}
            ),
            'request_notes':Textarea(
                attrs={'cols':4, 'rows':5, 'class':"form-control"}
            ),
        }


class PatientRadioReportForm(ModelForm):
    class Meta:
        model = PatientRadioReport
        fields = ['report']
        widgets = {
            'report':Textarea(
                attrs={'cols':4, 'rows':5, 'class':"form-control"}
            ),
        }
