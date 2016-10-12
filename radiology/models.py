from __future__ import unicode_literals

from django.db import models

from patient.models import Patient
from encounter.models import Encounter
from staff.models import Staff
# Create your models here.

class PatientRadioInvestigation(models.Model):
    encounter = models.ForeignKey(Encounter)
    requestor = models.ForeignKey(Staff, blank=True, null=True)
    request_notes = models.TextField("Notes", blank=True, null=True)
    request_time = models.DateTimeField(auto_now = True)
    reporter = models.ForeignKey(Staff, related_name='radiologist', null=True, blank=True)
    report_time = models.DateTimeField(auto_now = True)
    report_notes = models.TextField("Notes", blank=True, null=True)
    #status = models.ForeignKey(InvestigationStatus)
    image = models.CharField(max_length = 200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
