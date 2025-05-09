import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from .models import Admission
from .serializers import AdmissionSerializer
from .forms import AdmissionForm
from .logic.admission_logic import get_admissions, get_admission, create_admission

# from monitoring.auth0backend import getRole  # descomenta si ya tienes el archivo

def getRole(request):
    """Función de prueba temporal si no tienes auth0backend."""
    return request.user.groups.first().name if request.user.groups.exists() else "SinRol"

@login_required
def admission_list(request):
    role = getRole(request)
    if role in ["administrador", "medico"]:
        admissions = get_admissions()
        context = {
            'admission_list': admissions
        }
        return render(request, 'Admission/admissions.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def single_admission(request, id=0):
    role = getRole(request)
    if role in ["administrador", "medico"]:
        admission = get_admission(id)
        context = {
            'admission': admission
        }
        return render(request, 'Admission/admission.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def admission_create(request):
    role = getRole(request)
    if role == "administrador":
        if request.method == 'POST':
            form = AdmissionForm(request.POST)
        else:
            form = AdmissionForm()
        return render(request, 'Admission/admissionCreate.html', {'form': form})
    else:
        return HttpResponse("Unauthorized User")