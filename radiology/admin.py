from django.contrib import admin

from radiology.models import RequestStatus, PatientRadioRequest, PatientRadioReport

# Register your models here.

class RequestStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']    
    
class PatientRadioRequestAdmin(admin.ModelAdmin):
    list_display = ['encounter', 'requestor', 'clinical_summary', 'request_notes', 'request_status', 'request_time']

class PatientRadioReportAdmin(admin.ModelAdmin):
    list_display = ['request', 'report', 'reporter', 'report_time']


admin.site.register(RequestStatus, RequestStatusAdmin)
admin.site.register(PatientRadioRequest, PatientRadioRequestAdmin)
admin.site.register(PatientRadioReport, PatientRadioReportAdmin)
