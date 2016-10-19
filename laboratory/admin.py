from django.contrib import admin

# Register your models here.
from laboratory.models import DiagnosticServiceSection, Observation, ObservationGroup, PatientLabRequest, PatientLabReport

class DiagnosticServiceSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']

class ObservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'category', 'group', 'unit', 'maximum', 'minimum']
    list_filter = ['category', 'group']
    search_fields = ['name', 'code', 'category', 'group']

class ObservationGroupAdmin(admin.ModelAdmin):
    list_diplay = ['name', 'code']    

class PatientLabRequestAdmin(admin.ModelAdmin):
    list_display = ['requestor', 'request', 'request_notes', 'request_time', 'date_created', 'last_modified']
class PatientLabReportAdmin(admin.ModelAdmin):
    list_display = ['reporter', 'date_created']
    
admin.site.register(DiagnosticServiceSection, DiagnosticServiceSectionAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(ObservationGroup, ObservationGroupAdmin)
admin.site.register(PatientLabRequest, PatientLabRequestAdmin)
admin.site.register(PatientLabReport, PatientLabReportAdmin)
