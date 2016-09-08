from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from person.forms import PersonForm, PersonContactForm, PersonDemographicForm
from patient.models import Patient
from person.models import Prefix

# Create your views here.
def home(request):
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
        recently_added = Patient.objects.order_by('-date_created')[:5]
        
    return render(request, 'patient/index.html', {'form':form, 'recently_added':recently_added})


def to_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'patient/index.html')
        else:
            message = "Your account is inactive! Contact your Administrator"
            return render(request, 'dcare/index.html', {'error_message': message})
    else:
        message = "Invalid username and/or password"
        return render(request, 'dcare/index.html', {'error_message': message})
