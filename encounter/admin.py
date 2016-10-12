from django.contrib import admin

from encounter.models import Encounter, EncounterStatus, PatientVitals, Vitals
# Register your models here.

class EncounterStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']    
    
class EncounterAdmin(admin.ModelAdmin):
    list_display = ['patient', 'status', 'start_date', 'end_date']

class PatientVitalsAdmin(admin.ModelAdmin):
    list_display = ['encounter', 'measures']

class VitalsAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']



admin.site.register(Encounter, EncounterAdmin)
admin.site.register(EncounterStatus, EncounterStatusAdmin)
admin.site.register(PatientVitals, PatientVitalsAdmin)
admin.site.register(Vitals, VitalsAdmin)
