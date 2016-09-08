from django.contrib import admin

# Register your models here.
from patient.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'surname', 'othername']


admin.site.register(Patient, PatientAdmin)
