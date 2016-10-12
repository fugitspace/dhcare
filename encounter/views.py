from datetime import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from encounter.models import Encounter, EncounterStatus
from patient.models import Patient
# Create your views here.

# Create your views here.
def home(request):
    recently_added = Encounter.objects.order_by('-date_created')[:10]        
    return render(request, 'encounter/index.html', {'recently_added':recently_added})

def view_patient_encounter(request, patient_id):
    context = {}
    patient = Patient.objects.get(pk = patient_id)
    #history = EncounterPatientHistory.objects.filter()
    context['patient'] = patient

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
