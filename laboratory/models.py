from __future__ import unicode_literals

from django.db import models

from encounter.models import Encounter
from staff.models import Staff
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


class InvestigationStatus(models.Model):
    pass

class PatientLabInvestigation(models.Model):
    encounter = models.ForeignKey(Encounter)
    requestor = models.ForeignKey(Staff, related_name='medical_officer', null=True, blank=True)
    request_notes = models.TextField("Notes", blank=True, null=True)
    request_time = models.DateTimeField(auto_now = True)
    reporter = models.ForeignKey(Staff, null=True, blank=True)
    report_time = models.DateTimeField(auto_now=True)
    report_notes = models.TextField("Notes", blank=True, null=True)
    #status = models.ForeignKey(InvestigationStatus)    
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
