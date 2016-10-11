from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DiagnosticServiceSection(models.Model):
    '''Diagnostic Service Station according to FHIR like dermatology, '''
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class ObservationGroup(models.Model):
    '''Grouping of observations like: blood, urine, stool, etc'''
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    
class Observation(models.Model):
    '''A unique observation to be taken in the laboratory'''
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)    
    category = models.ForeignKey(DiagnosticServiceSection)
    group = models.ForeignKey(ObservationGroup, blank=True)
    unit = models.CharField(max_length=100, blank=True)
    maximum = models.CharField("Maximum Value", max_length=100, blank=True)
    minimum = models.CharField("Minimum Value", max_length=100, blank=True)

