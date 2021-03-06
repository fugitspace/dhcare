from datetime import datetime
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from encounter.models import Encounter, EncounterStatus, PatientVitals, Vitals, EncounterPatientHistory, EncounterPatientExamination, EncounterDiagnosis
from encounter.forms import PatientEncounterExamForm, PatientEncounterHistoryForm, EncounterDiagnosisForm
from patient.models import Patient
from radiology.models import PatientRadioRequest, PatientRadioReport, RequestStatus
from laboratory.models import PatientLabRequest, PatientLabReport, Observation
# Create your views here.
def home(request):
    recently_added = Encounter.objects.order_by('-date_created')[:10]        
    return render(request, 'encounter/index.html', {'recently_added':recently_added})

def view_patient_encounter(request, encounter_id):
    context = {}
    encounter = Encounter.objects.get(pk = encounter_id)
    patient = encounter.patient
    vital_measures = PatientVitals.objects.filter(encounter_id__exact=encounter_id).order_by('-date_created')[:1]
    history = EncounterPatientHistory.objects.filter(encounter_id__exact=encounter_id).order_by('-date_created')[:1]
    exam = EncounterPatientExamination.objects.filter(encounter_id__exact=encounter_id).order_by('-date_created')[:1]
    diagnosis = EncounterDiagnosis.objects.filter(encounter_id__exact=encounter_id).order_by('-date_created')[:1]
    radio_investigation = PatientRadioRequest.objects.filter(encounter_id__exact=encounter_id, request_status__code__iexact='new').order_by('-date_created', 'request_time')[:1]
    lab_request = PatientLabRequest.objects.filter(encounter_id__exact=encounter_id, request_status__code__iexact='new').order_by('-date_created', 'request_time')[:1]
    context['patient'] = patient
    context['encounter'] = encounter
    if len(history) != 0:
        context['history'] = history[0]
    if len(exam) != 0:
        context['exam'] = exam[0]
    if len(radio_investigation) != 0:
        context['radio_investigation'] = radio_investigation[0]
        report = PatientRadioReport.objects.filter(request_id__exact = radio_investigation[0].id)
        if len(report) > 0:
            context['radio_report'] = report[0]
    if len(lab_request) != 0:
        obs = json.loads(lab_request[0].request)
        print(obs)
        r_request = []
        for key, value in obs.iteritems():
            if key != 'csrfmiddlewaretoken':
                r_request.append(key)
        all_observations = Observation.objects.filter(id__in = r_request)
        requested_observations = {}
        for obs in all_observations:
            if requested_observations.has_key(obs.category.name):
                requested_observations[obs.category.name][obs.id] = obs
            else:
                requested_observations[obs.category.name] = {obs.id: obs}
        context['lab_request'] = requested_observations
        context['lab_request_id'] = lab_request[0].id
    if len(diagnosis) != 0:
        context['diagnosis'] = diagnosis[0]

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

def create_patient_encounter_history(request, encounter_id):
    form_title = "Patient History"
    if request.method == 'POST':
        form = PatientEncounterHistoryForm(request.POST)
        if form.is_valid():
            history = EncounterPatientHistory()
            history.history = request.POST['history']
            history.encounter = Encounter.objects.get(pk = encounter_id) 
            history.save()
            return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(encounter_id,)))
    else:
        form = PatientEncounterHistoryForm()
        
    return render(request, 'encounter/create_patient_encounter.html', {'form':form, 'form_title':form_title})

def edit_patient_encounter_history(request, history_id):
    form_title = "Edit Patient History"
    history = EncounterPatientHistory.objects.get(pk = history_id)
    if request.method == 'POST':
        form = PatientEncounterHistoryForm(request.POST, instance = history)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(history.encounter.id,)))
    else:
        form = PatientEncounterHistoryForm(instance = history)
        
    return render(request, 'encounter/create_patient_encounter.html', {'form':form, 'form_title':form_title})

def create_patient_encounter_exam(request, encounter_id):
    form_title = "Patient Exam"
    if request.method == 'POST':
        form = PatientEncounterExamForm(request.POST)
        if form.is_valid():
            exam = EncounterPatientExamination()
            exam.examination = request.POST['examination']
            exam.notes = request.POST['notes']
            exam.encounter = Encounter.objects.get(pk = encounter_id)
            exam.save()
            return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(encounter_id,)))
    else:
        form = PatientEncounterExamForm()
        
    return render(request, 'encounter/create_patient_encounter.html', {'form':form, 'form_title':form_title})

def edit_patient_encounter_exam(request, exam_id):
    form_title = "Edit Patient Exam"
    exam = EncounterPatientExamination.objects.get(pk = exam_id)
    if request.method == 'POST':
        form = PatientEncounterExamForm(request.POST, instance = exam)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(exam.encounter.id,)))
    else:
        form = PatientEncounterExamForm(instance = exam)
        
    return render(request, 'encounter/create_patient_encounter.html', {'form':form, 'form_title':form_title})

def create_patient_encounter_diagnosis(request, encounter_id):
    form_title = "Patient Diagnosis"
    if request.method == 'POST':
        form = EncounterDiagnosisForm(request.POST)
        if form.is_valid():
            diagnosis = EncounterDiagnosis()
            diagnosis.diagnosis = request.POST['diagnosis']
            diagnosis.notes = request.POST['notes']
            diagnosis.encounter = Encounter.objects.get(pk = encounter_id)
            diagnosis.save()
            return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(encounter_id,)))
    else:
        form = EncounterDiagnosisForm()
        
    return render(request, 'encounter/create_patient_encounter.html', {'form':form, 'form_title':form_title})

def edit_patient_encounter_diagnosis(request, diagnosis_id):
    form_title = "Edit Patient Diagnosis"
    diagnosis = EncounterDiagnosis.objects.get(pk = diagnosis_id)
    if request.method == 'POST':
        form = EncounterDiagnosisForm(request.POST, instance = diagnosis)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(diagnosis.encounter.id,)))
    else:
        form = EncounterDiagnosisForm(instance = diagnosis)
        
    return render(request, 'encounter/create_patient_encounter.html', {'form':form, 'form_title':form_title})

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
