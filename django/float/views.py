from django.shortcuts import render
from .models import Role, Place, Operator, Security, Message, IncidentPatient #, IncidentMessage
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You're at the project index!")