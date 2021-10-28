import json
from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.http.response import Http404, HttpResponse, JsonResponse
from django.core import serializers
from .models import Wilayah, RumahSakit

def index(request):
    dwilayah = Wilayah.objects.all()    
    drs = RumahSakit.objects.all()
    context = {
        'dwilayah': dwilayah,
        'drs': drs,
    }

    return render(request, 'rujukan/rumah_sakit_rujukan.html', context)
