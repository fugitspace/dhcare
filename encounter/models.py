from __future__ import unicode_literals
from datetime import datetime

from django.utils import timezone
from django.db import models

from patient.models import Patient
# Create your models here.

class EncounterStatus(models.Model):
    '''The status of an encounter:
    planned: appointment
    in_progress: patient is being attended
    finished: patient is discharged
    cancelled: encounter ended before completion'''
    name = models.CharField("Display Name", max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.code

class Encounter(models.Model):
    '''The actual encounter, when a patient meets a practitioner or visits
    a service provider/point of care'''
    patient = models.ForeignKey(Patient)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(EncounterStatus)
    notes = models.TextField("Special Notes", blank=True, max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now = True, null=True)
    
    def __str__(self):
        return self.status    

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

class PatientEncounterVitals(models.Model):
    patientvitals = models.ForeignKey(PatientVitals, blank=True, null=True)
    encounter = models.ForeignKey(Encounter, blank=True, null=True)
    
class EncounterPatientHistory(models.Model):
    '''History recorded for this patient for this encounter'''
    encounter = models.ForeignKey(Encounter)
    history = models.TextField(max_length=500, blank=True, verbose_name="History")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Encounter History'

class EncounterPatientExamination(models.Model):
    '''Examinations performed during this enconter'''
    encounter = models.ForeignKey(Encounter)
    examination = models.TextField(max_length=500, blank=True, verbose_name="Examination")
    notes = models.TextField("Special Notes", blank=True, max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Encounter Examinations'

class EncounterDiagnosis(models.Model):
    '''Diagnosis for this encounter'''
    encounter = models.ForeignKey(Encounter)
    diagnosis = models.TextField(max_length=500, blank=True, verbose_name="Diagnosis")
    notes = models.TextField("Special Notes", blank=True, max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Encounter Diagnoses'
        
'''class EncounterTreatment(models.Model):
    ''Treatment provided during this encounter''
    encounter = models.ForeignKey(Encounter)
    treatment = models.TextField(max_length=500, blank=True, verbose_name="Treatment")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Encounter Treatment'
'''
