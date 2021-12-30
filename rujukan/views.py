import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Wilayah, RumahSakit
from .forms import RSForm

def index(request):
    dwilayah = Wilayah.objects.all()    
    drs = RumahSakit.objects.all()
    context = {
        'dwilayah': dwilayah,
        'drs': drs,
    }

    return render(request, 'rujukan/rumah_sakit_rujukan.html', context)

@login_required(login_url="/admin/login/")
def add(request):
    if request.method == 'POST':
        form = RSForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rumah-sakit-rujukan')
    else:
        form = RSForm()
    
    return render(request, 'rujukan/rujukan_forms.html', {'form': form})

def jsonRS(request):

    rss = dict()
    for ob in Wilayah.objects.all():
        rss[ob.nama] = json.loads(serializers.serialize('json', Wilayah.objects.get(nama=ob.nama).daftarRS.all()))

    print(rss)
    data = json.dumps(rss)
    return HttpResponse(data, content_type="application/json")

def jsonWilayah(request):

    data = serializers.serialize('json', Wilayah.objects.all())
    return HttpResponse(data, content_type="application/json")