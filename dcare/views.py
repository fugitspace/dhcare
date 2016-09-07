from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
#from dcare import http


def index(request):
  
  return render(request, 'dcare/index.html')
