from django.shortcuts import render
from .models import Kategori
from django.http.response import HttpResponse
from django.core import serializers

def vaksinasi(request):
    kategoris = Kategori.objects.all().values()
    context = {'kategoris': kategoris}
    return render(request, 'vaksinasi.html', context)

def kategori(request):
    data = serializers.serialize('json', Kategori.objects.all())
    return HttpResponse(data, content_type="application/json")