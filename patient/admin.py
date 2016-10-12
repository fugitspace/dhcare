from django.contrib import admin

# Register your models here.
from patient.models import Patient, PatientDemographic, PatientContact

class PatientAdmin(admin.ModelAdmin):
    list_display = ['id_number', 'firstname', 'surname', 'othername']

class PatientDemographicAdmin(admin.ModelAdmin):
    list_display = ['person', 'gender', 'birthdate', 'marital_status', 'religion']

class PatientContactAdmin(admin.ModelAdmin):
    list_display = ['person', 'mobile', 'alt_mobile', 'telephone', 'email', 'mailing_address']

class PatientRelativeAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'surname', 'othername']

admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientDemographic, PatientDemographicAdmin)
admin.site.register(PatientContact, PatientContactAdmin)
