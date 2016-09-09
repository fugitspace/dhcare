from __future__ import unicode_literals

from django.db import models

#external models
from person.models import Person, PersonDemographic, PersonContact

# Create your models here.

class Patient(Person):
    pass

class PatientDemographic(PersonDemographic):
    pass

class PatientContact(PersonContact):
    pass

class PatientVitals(models.Model):
    patient = models.ForeignKey(Patient)
    measures = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Patient Vitals"

        
class Vitals(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default = True)

    class Meta:
        verbose_name_plural = "Vitals"
