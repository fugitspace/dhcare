from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from person.forms import PersonForm, PersonContactForm, PersonDemographicForm
from patient.models import Patient
from person.models import Prefix

# Create your views here.
def home(request):
    recently_added = Patient.objects.order_by('-date_created')[:5]        
    return render(request, 'patient/index.html', {'recently_added':recently_added})


def create_patient(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            if len(request.POST['id']) == 0:
                print("we are creating a new")
                patient = Patient()
            else:
                patient = Patient.objects.get(pk=request.POST['id'])
            patient.surname = request.POST['surname']
            patient.firstname = request.POST['firstname']
            patient.othername = request.POST['othername']
            print(request.POST['othername'])
            print(request.POST['prefix'])
            patient.prefix = Prefix.objects.get(id=request.POST['prefix'])
            patient.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(patient.id,)))
    else:
        form = PersonForm()
        
    return render(request, 'patient/create_patient.html', {'form':form})    

def edit_patient(request, patient_id):    
    
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            patient = Patient.objects.get(pk=patient_id)
            patient.surname = request.POST['surname']
            patient.firstname = request.POST['firstname']
            patient.othername = request.POST['othername']
            patient.prefix = Prefix.objects.get(id=request.POST['prefix'])
            patient.save()
            return HttpResponseRedirect(reverse('patient:view_patient', args=(patient.id,)))
    else:
        form = PersonForm()
        
    return render(request, 'patient/create_patient.html', {'form':form})

def view_patient(request, patient_id):
    patient = Patient.objects.get(pk = patient_id)
    
    return render(request, 'patient/view_patient.html', {'patient':patient})
