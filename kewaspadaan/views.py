from django.shortcuts import render
from .models import Indikator
from .forms import SaranForm

def kewaspadaan(request):
    return render(request, 'index_kewaspadaan.html')
