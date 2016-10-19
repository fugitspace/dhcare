from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from radiology.models import PatientRadioReport, PatientRadioRequest, RequestStatus
from radiology.forms import PatientRadioReportForm, PatientRadioRequestForm
from encounter.models import Encounter
# Create your views here.


def home(request):
    pending_requests = PatientRadioRequest.objects.filter(request_status__code__iexact='new').order_by('-date_created', 'request_time')
    return render(request, 'radiology/index.html', {'pending_requests':pending_requests})

def view_patient_radio_requests(request, encounter_id):
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
    return render(request, 'radiology/view_patient_radio_requests.html', context)

def create_radiology_request(request, encounter_id):
    form_title = "Radiology Request"
    if request.method == 'POST':
        form = PatientRadioRequestForm(request.POST)
        if form.is_valid():
            radio_request = PatientRadioRequest()
            radio_request.clinical_summary = request.POST['clinical_summary']
            radio_request.request_notes = request.POST['request_notes']
            radio_request.requestor = request.user
            radio_request.request_status = RequestStatus.objects.get(code = 'new')
            radio_request.encounter = Encounter.objects.get(pk = encounter_id)            
            radio_request.save()
            return HttpResponseRedirect(reverse('radiology:home'))
    else:
        form = PatientRadioRequestForm()
        
    return render(request, 'radiology/create_radiology_request.html', {'form':form, 'form_title':form_title})

def edit_radiology_request(request, history_id):
    form_title = "Edit Radiology Request"
    history = EncounterPatientHistory.objects.get(pk = history_id)
    if request.method == 'POST':
        form = PatientEncounterHistoryForm(request.POST, instance = history)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('encounter:view_patient_encounter', args=(history.encounter.id,)))
    else:
        form = PatientEncounterHistoryForm(instance = history)
        
    return render(request, 'encounter/create_patient_encounter.html', {'form':form, 'form_title':form_title})
