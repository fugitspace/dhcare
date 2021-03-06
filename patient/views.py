import json
from datetime import date, datetime

from reportlab.pdfgen import canvas

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Q

from person.forms import PersonForm, PersonContactForm, PersonDemographicForm, PersonRelativeForm
from patient.models import Patient, PatientDemographic, PatientContact, PatientRelative
from person.models import Prefix, MaritalStatus, Gender, Religion, Relationship
from encounter.models import Encounter, EncounterStatus, Vitals, PatientVitals
from encounter.forms import PatientVitalsForm

# Create your views here.
def home(request):
    recently_added = Patient.objects.order_by('-date_created')[:10]        
    return render(request, 'patient/index.html', {'recently_added':recently_added})

def search_patient(request):    
    if request.is_ajax():
        q = request.GET['q']
        print "Search for ", q
        if q is not None:
            patients = Patient.objects.filter(
                Q(firstname__icontains = q) |
                Q(surname__icontains = q) |
                Q(othername__icontains = q)
                ).order_by('firstname')
            
            return render(request, 'patient/search_patient.html', {'patients_found':patients})
    else:
        print "request was not ajax"
            
def view_patient(request, patient_id):
    context = {}
    patient = Patient.objects.get(pk = patient_id)
    vital_measures = PatientVitals.objects.filter(encounter__patient__id__exact=patient_id).order_by('-date_created')[:1]
    demographic_info = PatientDemographic.objects.filter(person_id__exact=patient_id)
    contact_info = PatientContact.objects.filter(person_id__exact=patient_id)
    relative_info = PatientRelative.objects.filter(person_id__exact=patient_id)
    encounter = Encounter.objects.filter(patient_id__exact = patient_id).order_by('-start_date')[:1]
        
    context['patient'] = patient

    if len(contact_info) != 0:        
        context['contact'] = contact_info[0]

    if len(relative_info) != 0:        
        context['relative'] = relative_info[0]
        
    if len(encounter) != 0:        
        context['encounter'] = encounter[0]
        
    if len(demographic_info) != 0:        
        context['demographic'] = demographic_info[0]
        
    if len(vital_measures) != 0:
        record_date = vital_measures[0].date_created
        v_id = vital_measures[0].id
        vital_measures = json.loads(vital_measures[0].measures)
        patient_vitals = {}
        for key, measure in vital_measures.iteritems():
            if key != 'csrfmiddlewaretoken':
                patient_vitals[get_object_or_404(Vitals, pk=int(key)).name] = measure
        context['patient_vitals'] = patient_vitals
        context['patient_vitals_id'] = v_id
        context['record_date'] = record_date          
    return render(request, 'patient/view_patient.html', context)


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
            patient.id_number = "{}-{}".format(date.today().strftime('%Y-%m'), 1 if len(Patient.objects.all()) == 0 else (Patient.objects.all().order_by('-id')[0].id)+1)
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

def edit_patient_demographic(request, demographic_id):
    form_title = "Edit Patient Demographic"
    demographic = get_object_or_404(PatientDemographic, pk=demographic_id)
    if request.method == 'POST':
        form = PersonDemographicForm(request.POST, instance = demographic)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(demographic.person.id,)))
    else:
        form = PersonDemographicForm(instance = demographic)
        
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


def edit_patient_contact(request, contact_id):
    form_title = "Edit Patient Contact"
    contact = get_object_or_404(PatientContact, pk=contact_id)
    if request.method == 'POST':
        form = PersonContactForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(contact.person.id,)))
    else:
        form = PersonContactForm(instance = contact)

    return render(request, 'patient/create_patient_contact.html', {'form':form, 'form_title':form_title})

def create_patient_relative(request, patient_id):
    form_title = "Patient Relative"
    if request.method == 'POST':
        form = PersonRelativeForm(request.POST)
        if form.is_valid():
            relative = PatientRelative()
            relative.mobile = request.POST['mobile']
            relative.full_name = request.POST['full_name']
            relative.relationship = Relationship.objects.get(pk = request.POST['relationship'])
            relative.alt_mobile = request.POST['alt_mobile']
            relative.telephone = request.POST['telephone']
            relative.email = request.POST['email']
            relative.mailing_address = request.POST['mailing_address']
            patient = get_object_or_404(Patient, pk=patient_id)
            relative.person = patient            
            relative.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(patient.id,)))
    else:
        form = PersonRelativeForm()
        
    return render(request, 'patient/create_patient_relative.html', {'form':form, 'form_title':form_title}) 

def edit_patient_relative(request, relative_id):
    form_title = "Patient Relative"
    relative = get_object_or_404(PatientRelative, pk = relative_id)
    if request.method == 'POST':
        form = PersonRelativeForm(request.POST, instance = relative)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(relative.person.id,)))
    else:
        form = PersonRelativeForm(instance = relative)
        
    return render(request, 'patient/create_patient_relative.html', {'form':form, 'form_title':form_title})


def edit_patient_vitals(request, patient_vitals_id):
    form_title = "Patient Vitals Registration"
    patient_vitals = get_object_or_404(PatientVitals, pk = patient_vitals_id)
    if request.method == 'POST':        
        patientvitals = json.dumps(request.POST)        
        patient_vitals.measures = patientvitals        
        patient_vitals.save(update_fields=['measures'])
        return HttpResponseRedirect(reverse('patient:view_patient', args=(patient_vitals.encounter.patient.id,)))
    else:
        vitals = Vitals.objects.all()
        fields = {}
        for vital in vitals:
            fields[vital.id] = vital.name
        print(patient_vitals.measures)
        measures = json.loads(patient_vitals.measures)
        vital_fields = {}
        for vital_key, value in measures.iteritems():
            if vital_key != 'csrfmiddlewaretoken':
                vital_fields[int(vital_key)] = {'label':fields[int(vital_key)], 'value':value}
        
    return render(request, 'patient/edit_patient_vitals.html', {'form':vital_fields, 'edit':1, 'form_title':form_title}) 

def create_patient_vitals(request, patient_vitals_id):
    form_title = "Patient Vitals Registration"
    if request.method == 'POST':
        patient = get_object_or_404(Patient, pk=patient_id)
        encounter = Encounter()
        encounter.patient = patient
        encounter.start_date = datetime.now()
        encounter.status = EncounterStatus.objects.get(code='in-progress')        
        encounter.save()
        
        patientvitals = json.dumps(request.POST)
        patientObject = get_object_or_404(Patient, pk=patient_id)
        pVital = PatientVitals()
        pVital.measures = patientvitals
        #pVital.patient = patientObject # vitals belong to an encounter which belongs to a person
        pVital.encounter = encounter
        pVital.save()
        return HttpResponseRedirect(reverse('patient:view_patient', args=(patient_id,)))
    else:
        vitals = Vitals.objects.filter(active__exact = 1)
        vital_fields = {}
        for vital in vitals:
            vital_fields[vital.id] = vital.name
        
    return render(request, 'patient/create_patient_vitals.html', {'form':vital_fields, 'form_title':form_title})


def patient_index_card(request, patient_id):
    patientObj = Patient.objects.get(pk=patient_id)
    full_name = patientObj.surname+"_"+patientObj.firstname+".pdf"
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+full_name
    
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(10, 100, "KILA MARA UFIKAPO HOSPITALINI HAKIKISHA UMEKILETA.")
    p.drawString(10, 90, "Namba ya Hospitali: "+str(patientObj.id))
    p.drawString(10, 80, "Jina la Ukoo: "+patientObj.surname)
    p.drawString(10, 70, "Majina Mengine: "+patientObj.firstname)
    p.drawString(10, 60, "Tarehe ya Kuzaliwa: "+str(PatientDemographic.objects.get(person_id__exact=patient_id).birthdate))
    
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
