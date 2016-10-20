import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from laboratory.models import PatientLabRequest, PatientLabReport, Observation
from radiology.models import RequestStatus
#from laboratory.forms import PatientLabRequestForm, PatientLabReportForm
from encounter.models import Encounter
# Create your views here.


def home(request):
    pending_requests = PatientLabRequest.objects.filter(request_status__code__iexact='new').order_by('-date_created', 'request_time')
    return render(request, 'laboratory/index.html', {'pending_requests':pending_requests})

def view_patient_lab_requests(request, encounter_id):
    context = {}
    encounter = Encounter.objects.get(pk = encounter_id)    
    radio_investigation = PatientRadioRequest.objects.filter(encounter_id__exact=encounter_id).order_by('-date_created', 'request_time')
    
    if request.method == 'POST':
        form = PatientRadioReportForm(request.POST)
        if form.is_valid():
            radio_report = PatientRadioReport()
            radio_report.reporter = request.user
            radio_report.report = request.POST['report']
            radio_report.request = radio_investigation[0]
            radio_report.save()            

    radio_report = PatientRadioReport.objects.filter(request_id__exact=radio_investigation[0].id)
    
    context['patient'] = encounter.patient 
    if len(radio_investigation) != 0:
        context['radio_investigation'] = radio_investigation[0]
    if len(radio_report) == 0:
        form = PatientRadioReportForm()
        context['form'] = form
    else:
        context['radio_report'] = radio_report[0]
    return render(request, 'laboratory/view_patient_lab_requests.html', context)

def create_lab_request(request, encounter_id):
    form_title = "Lab Request"
    if request.method == 'POST':
        encounter = get_object_or_404(Encounter, pk=encounter_id)
        labRequest = PatientLabRequest()
        requests = json.dumps(request.POST)
        labRequest.request = requests        
        labRequest.requestor = request.user
        labRequest.encounter = encounter
        labRequest.request_status = RequestStatus.objects.get(code = 'new')
        labRequest.save()
        return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(encounter_id,)))
    else:
        observations = Observation.objects.filter(active__exact = 1)
        form = {}
        for observation in observations:
            if form.has_key(observation.category.name):
                form[observation.category.name][observation.id] = observation.name
            else:
                form[observation.category.name] = {observation.id: observation.name}
            print(form)
        return render(request, 'laboratory/create_lab_request.html', {'form':form, 'form_title':form_title})

def edit_lab_request(request, request_id):
    form_title = "Edit Lab Report"
    
    report = PatientRadioReport.objects.get(pk = report_id)
    radio_request = report.request
    encounter = radio_request.encounter
    if request.method == 'POST':
        requests = []
        for key, value in request.POST.iteritems():
            if key != 'csrfmiddlewaretoken':
                requests.append(int(key)) 
        labRequest.request = requests        
        labRequest.requestor = request.user
        labRequest.save(update_fields=['request', 'requestor'])
        return HttpResponseRedirect(reverse('laboratory:view_patient_lab_requests', args=(report.request.encounter.id,)))
    else:
        observations = Observation.objects.filter(active__exact = 1)
        form = {}
        for observation in observations:
            if form.has_key(observation.category.name):
                form[observation.category.name][observation.id] = observation.name
            else:
                form[observation.category.name] = {observation.id: observation.name}
            print(form)
    return render(request, 'laboratory/edit_patient_lab_report.html', {'form':form, 'edit':1, 'form_title':form_title})


def edit_lab_report(request, history_id):
    form_title = "Edit Lab Request"
    history = EncounterPatientHistory.objects.get(pk = history_id)
    if request.method == 'POST':
        form = PatientEncounterHistoryForm(request.POST, instance = history)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(history.encounter.id,)))
    else:
        form = PatientEncounterHistoryForm(instance = history)
        
    return render(request, 'encounter/create_patient_encounter.html', {'form':form, 'form_title':form_title})
