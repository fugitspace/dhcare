from datetime import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from encounter.models import Encounter, EncounterStatus, PatientVitals, Vitals
from patient.models import Patient
# Create your views here.

# Create your views here.
def home(request):
    recently_added = Encounter.objects.order_by('-date_created')[:10]        
    return render(request, 'encounter/index.html', {'recently_added':recently_added})

def view_patient_encounter(request, encounter_id):
    context = {}
    encounter = Encounter.objects.get(pk = encounter_id)
    patient = encounter.patient
    vital_measures = PatientVitals.objects.filter(encounter_id__exact=encounter_id).order_by('-date_created')[:1]
    #history = EncounterPatientHistory.objects.filter()
    context['patient'] = patient
    if len(vital_measures) != 0:
        record_date = vital_measures[0].date_created
        vital_measures = json.loads(vital_measures[0].measures)
        patient_vitals = {}
        for key, measure in vital_measures.iteritems():
            if key != 'csrfmiddlewaretoken':
                patient_vitals[get_object_or_404(Vitals, pk=int(key)).name] = measure
                context['patient_vitals'] = patient_vitals
                context['record_date'] = record_date
    return render(request, 'encounter/view_patient_encounter.html', context)


def new_encounter(request, patient_id):
    if request.is_ajax():
        patient = get_object_or_404(Patient, pk=patient_id)
        encounter = Encounter()
        encounter.patient = patient
        encounter.start_date = datetime.now()
        encounter.status = EncounterStatus.objects.get(code='in-progress')
        encounter.save()
        return HttpResponse(
            json.dumps({'encounter':encounter}),
            content_type='application/json'
        )

def end_encounter(request, encounter_id):
    if request.is_ajax():
        encounter = get_object_or_404(Encounter, pk=encounter_id)        
        encounter.patient = patient
        encounter.end_date = datetime.now()
        encounter.status = EncounterStatus.objects.get(code='finished')
        encounter.save()
        return HttpResponse(
            json.dumps({'encounter':encounter}),
            content_type='application/json'
        )
