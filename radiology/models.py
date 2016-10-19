from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from encounter.models import Encounter
from django.contrib.auth.models import User
# Create your models here.

class RequestStatus(models.Model):
    '''Request status can be new, in-progress, completed'''
    name = models.CharField(max_length = 20)
    code = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    
class PatientRadioRequest(models.Model):
    encounter = models.ForeignKey(Encounter)
    requestor = models.ForeignKey(User, blank=True, null=True)
    clinical_summary = models.TextField("Clinical Summary")
    request_notes = models.TextField("X-Ray requested/USS")
    request_status = models.ForeignKey(RequestStatus)
    request_time = models.TimeField(default = timezone.now)    
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "{} - {}".format(self.encounter.patient.firstname, self.request_time)
    
class PatientRadioReport(models.Model):
    request = models.ForeignKey(PatientRadioRequest)
    report = models.TextField("Report", blank=True, null=True)
    reporter = models.ForeignKey(User, related_name='radiologist', null=True, blank=True)
    report_time = models.TimeField(default=timezone.now)   
    image_url = models.CharField("Image", max_length = 200, blank=True, null=True)
    thumbnail_url = models.CharField("Image", max_length = 200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


    def __str__(self):
        return "{} - {}".format(self.request.encounter.patient.firstname, self.report_time)
