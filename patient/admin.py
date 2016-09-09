from django.contrib import admin

# Register your models here.
from patient.models import Patient, PatientDemographic, PatientContact, PatientVitals, Vitals

class PatientAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'surname', 'othername']

class PatientDemographicAdmin(admin.ModelAdmin):
    list_display = ['person', 'gender', 'birthdate', 'marital_status', 'religion']

class PatientContactAdmin(admin.ModelAdmin):
    list_display = ['person', 'mobile', 'alt_mobile', 'telephone', 'email', 'mailing_address']


class PatientVitalsAdmin(admin.ModelAdmin):
    list_display = ['patient', 'measures']

class VitalsAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']


class PatientRelativeAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'surname', 'othername']

admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientDemographic, PatientDemographicAdmin)
admin.site.register(PatientContact, PatientContactAdmin)
admin.site.register(PatientVitals, PatientVitalsAdmin)
admin.site.register(Vitals, VitalsAdmin)
