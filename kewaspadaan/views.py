from django.shortcuts import render
from .models import Indikator
from django.contrib.auth.decorators import login_required
from .forms import SaranForm

import json
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def jsonWaspada(request):
    data = serializers.serialize('json', Indikator.objects.all())
    return HttpResponse(data, content_type="application/json")

def kewaspadaan(request):
    indikators = Indikator.objects.all()
    context = {'indikators': indikators}
    return render(request, 'index_kewaspadaan.html', context)

@login_required(login_url="/admin/login/")
def add(request):
    form = SaranForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'index_kewaspadaan_form.html', {'form':form})