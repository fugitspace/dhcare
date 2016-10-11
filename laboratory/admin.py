from django.contrib import admin

# Register your models here.
from laboratory.models import DiagnosticServiceSection, Observation, ObservationGroup

class DiagnosticServiceSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']

class ObservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'category', 'unit', 'maximum', 'minimum']
    list_filter = ['category', 'group']
    search_fields = ['name', 'code', 'category', 'group']

class ObservationGroupAdmin(admin.ModelAdmin):
    list_diplay = ['name', 'code']    

admin.site.register(DiagnosticServiceSection, DiagnosticServiceSectionAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(ObservationGroup, ObservationGroupAdmin)
