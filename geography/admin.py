from django.contrib import admin

# Register your models here.
from geography.models import Country, Region, District, Ward

class CountryAdmin(admin.ModelAdmin):
  list_display = ["name", "iso_3code", "iso_2code", "last_modified"]
  search_fields = ["name", "iso_3code"]

class RegionAdmin(admin.ModelAdmin):
  list_display = ["name", "code", "country", "last_modified"]
  search_fields = ["name"]

class DistrictAdmin(admin.ModelAdmin):
  list_display = ["name", "code", "last_modified"]
  search_fields = ["name", "code"]

class WardAdmin(admin.ModelAdmin):
  list_display = ["name", "code", "last_modified"]
  search_fields = ["name", "code"]

admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Ward, WardAdmin)
