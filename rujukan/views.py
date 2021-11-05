import json
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
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
            return HttpResponseRedirect('rujukan/rumah_sakit_rujukan.html')
    else:
        form = RSForm()
    
    return render(request, 'rujukan/rujukan_forms.html', {'form': form})
