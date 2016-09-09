import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from person.forms import PersonForm, PersonContactForm, PersonDemographicForm
from patient.forms import PatientVitalsForm
from patient.models import Patient, PatientDemographic, PatientContact, Vitals, PatientVitals
from person.models import Prefix, MaritalStatus, Gender, Religion

# Create your views here.
def home(request):
    recently_added = Patient.objects.order_by('-date_created')[:5]        
    return render(request, 'patient/index.html', {'recently_added':recently_added})


def create_patient(request):
    form_title = "Add New Patient"
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            patient = Patient()
            patient.surname = request.POST['surname']
            patient.firstname = request.POST['firstname']
            patient.othername = request.POST['othername']
            patient.prefix = Prefix.objects.get(pk = request.POST['prefix'])
            patient.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(patient.id,)))
    else:
        form = PersonForm()
        
    return render(request, 'patient/create_patient.html', {'form':form, 'form_title':form_title})    

def edit_patient(request, patient_id):
    form_title = 'Edit Patient Information'
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance = patient)
        if form.is_valid():            
            form.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(patient.id,)))
    else:
        form = PersonForm(instance = patient)
        
    return render(request, 'patient/create_patient.html', {'form':form, 'form_title':form_title})

def view_patient(request, patient_id):
    context = {}
    patient = Patient.objects.get(pk = patient_id)
    vital_measures = PatientVitals.objects.filter(patient__id__exact=patient_id).order_by('-date_created')[:1]
    demographic_info = PatientDemographic.objects.filter(person_id__exact=patient_id)
    contact_info = PatientContact.objects.filter(person_id__exact=patient_id)
    print contact_info
    context['patient'] = patient

    if len(contact_info) != 0:
        context['contact'] = contact_info[0]
        
    if len(demographic_info) != 0:        
        context['demographic'] = demographic_info[0]
        
    if len(vital_measures) != 0:
        record_date = vital_measures[0].date_created
        vital_measures = json.loads(vital_measures[0].measures)
        patient_vitals = {}
        for key, measure in vital_measures.iteritems():
            if key != 'csrfmiddlewaretoken':
                patient_vitals[get_object_or_404(Vitals, pk=int(key)).name] = measure
                context['patient_vitals'] = patient_vitals
                context['record_date'] = record_date          
    return render(request, 'patient/view_patient.html', context)


################ Patient Demographic ###########################

def create_patient_demographic(request, patient_id):
    form_title = "Patient Demographic"
    if request.method == 'POST':
        form = PersonDemographicForm(request.POST)
        if form.is_valid():
            patient = PatientDemographic()
            patient.person = get_object_or_404(Patient, pk=patient_id)
            patient.gender = Gender.objects.get(pk = request.POST['gender'])
            patient.marital_status = MaritalStatus.objects.get(pk = request.POST['marital_status'])
            patient.religion = Religion.objects.get(pk = request.POST['religion'])
            patient.birthdate = request.POST['birthdate']
            patient.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(patient_id,)))
    else:
        form = PersonDemographicForm()
        
    return render(request, 'patient/create_patient_demographic.html', {'form':form, 'form_title':form_title}) 

def create_patient_contact(request, patient_id):
    form_title = "Patient Contact"
    if request.method == 'POST':
        form = PersonContactForm(request.POST)
        if form.is_valid():
            contact = PatientContact()
            contact.mobile = request.POST['mobile']
            contact.alt_mobile = request.POST['alt_mobile']
            contact.telephone = request.POST['telephone']
            contact.email = request.POST['email']
            contact.mailing_address = request.POST['mailing_address']
            patient = get_object_or_404(Patient, pk=patient_id)
            contact.person = patient            
            contact.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(patient.id,)))
    else:
        form = PersonContactForm()
        
    return render(request, 'patient/create_patient_contact.html', {'form':form, 'form_title':form_title})

def create_patient_relative(request):
    form_title = "Add New Patient"
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            patient = Patient()
            patient.surname = request.POST['surname']
            patient.firstname = request.POST['firstname']
            patient.othername = request.POST['othername']
            patient.prefix = Prefix.objects.get(pk = request.POST['prefix'])
            patient.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(patient.id,)))
    else:
        form = PersonForm()
        
    return render(request, 'patient/create_patient_relative.html', {'form':form, 'form_title':form_title}) 


def create_patient_vitals(request, patient_id):
    form_title = "Patient Vitals Registration"
    if request.method == 'POST':
        patientvitals = json.dumps(request.POST)
        print patientvitals
        patientObject = get_object_or_404(Patient, pk=patient_id)
        pVital = PatientVitals()
        pVital.measures = patientvitals
        pVital.patient = patientObject
        pVital.save()
        return HttpResponseRedirect(reverse('patient:view_patient', args=(patient_id,)))
    else:
        vitals = Vitals.objects.filter(active__exact = 1)
        vital_fields = {}
        for vital in vitals:
            vital_fields[vital.id] = vital.name
        
    return render(request, 'patient/create_patient_vitals.html', {'form':vital_fields, 'form_title':form_title}) 

def view_patient_vitals(request, patient_id):
    patientObj = PatientVitals.objects.filter(patient__id__exact=patient_id)

    return render(request, 'patient/view_patient.html', 'patient')
