from django.shortcuts import render
from .models import Indikator
from django.contrib.auth.decorators import login_required
from .forms import SaranForm

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