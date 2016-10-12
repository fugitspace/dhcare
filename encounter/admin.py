from django.contrib import admin

from encounter.models import Encounter, EncounterStatus
# Register your models here.

class EncounterStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']    
    
class EncounterAdmin(admin.ModelAdmin):
    list_display = ['patient', 'status', 'start_date', 'end_date']
    

admin.site.register(Encounter, EncounterAdmin)
admin.site.register(EncounterStatus, EncounterStatusAdmin)
