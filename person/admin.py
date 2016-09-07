from django.contrib import admin

# Register your models here.

from person.models import Person, PersonDemographic, PersonPhoto, PersonContact, Gender, MaritalStatus, Religion, Prefix


class PersonAdmin(admin.ModelAdmin):
    list_display = ['surname', 'firstname', 'othername', 'prefix', 'last_modified']
    search_fields = ['surname', 'firstname', 'othername',]

class PersonDemographicAdmin(admin.ModelAdmin):
    list_display = ['person', 'gender', 'birthdate', 'marital_status', 'religion']

class PersonPhotoAdmin(admin.ModelAdmin):
    list_display = ['person', 'photo']

class PersonContactAdmin(admin.ModelAdmin):
    list_display = ['person', 'mobile', 'telephone', 'alt_mobile', 'email']

class GenderAdmin(admin.ModelAdmin):
    list_display = ['name']

class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_modified']

class ReligionAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_modified']

class PrefixAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_modified']
    
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonDemographic, PersonDemographicAdmin)
admin.site.register(PersonPhoto, PersonPhotoAdmin)
admin.site.register(PersonContact, PersonContactAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(MaritalStatus, MaritalStatusAdmin)
admin.site.register(Religion, ReligionAdmin)
admin.site.register(Prefix, PrefixAdmin)
