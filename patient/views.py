from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
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
            patient = Patient()
            patient.surname = request.POST['surname']
            patient.firstname = request.POST['firstname']
            patient.othername = request.POST['othername']
            print(request.POST['othername'])
            print(request.POST['prefix'])
            patient.prefix = Prefix.objects.get(id=request.POST['prefix'])
            patient.save()
            return HttpResponseRedirect('/patient/')
    else:
        form = PersonForm()
        
    return render(request, 'patient/create_patient.html', {'form':form})    


def view_patient(request):
    patient_id = request.GET['patient_id']
    patient = Patient.objects.get(id = patient_id)
    
    return render(request, 'patient/view_patient.html', {'patient':patient})
