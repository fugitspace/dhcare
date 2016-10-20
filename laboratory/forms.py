from django.forms import ModelForm, Textarea, TextInput, Select
from laboratory.models import PatientLabRequest, PatientLabReport

class PatientLabRequestForm(ModelForm):
    class Meta:
        model = PatientLabRequest
        fields = ['request']


class PatientlabReportForm(ModelForm):
    class Meta:
        model = PatientLabReport
        fields = ['report']
