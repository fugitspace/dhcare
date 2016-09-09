from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from person.forms import PersonForm, PersonContactForm, PersonDemographicForm
from patient.models import Patient
from person.models import Prefix

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
    patient = Patient.objects.get(pk = patient_id)
    
    return render(request, 'patient/view_patient.html', {'patient':patient})
