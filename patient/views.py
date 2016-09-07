# Authentication
from django.contrib.auth import authenticate, login

#http requests
from django.shortcuts import render

# Create your views here.
def home(request):
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
