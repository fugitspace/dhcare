from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField("Country Name", max_length=200)
    alpha_two = models.CharField("2-Letter Code", max_length=2, blank=True)
    alpha_three = models.CharField("3-Letter Code", max_length=3, blank=True)
    date_created = models.DateTimeField("Date Published", auto_now_add=True)
    last_modified = models.DateTimeField("Last Updated", auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.alpha_two)

    class Meta:
        verbose_name_plural = 'Countries'

        
class Region(models.Model):
    name = models.CharField("Region Name", max_length=200)
    code = models.CharField("Abbreviation", max_length=200, blank=True)
    country = models.ForeignKey(Country)
    date_created = models.DateTimeField("Date Published", auto_now_add=True)
    last_modified = models.DateTimeField("Last Updated", auto_now=True)

class District(models.Model):
    name = models.CharField("District Name", max_length=200)
    code = models.CharField("Abbreviation", max_length=200, blank=True)
    region = models.ForeignKey(Region)
    date_created = models.DateTimeField("Date Published", auto_now_add=True)
    last_modified = models.DateTimeField("Last Updated", auto_now=True)

class Ward(models.Model):
    name = models.CharField("District Name", max_length=200)
    code = models.CharField("Abbreviation", max_length=200, blank=True)
    district = models.ForeignKey(District)
    date_created = models.DateTimeField("Date Published", auto_now_add=True)
    last_modified = models.DateTimeField("Last Updated", auto_now=True)
