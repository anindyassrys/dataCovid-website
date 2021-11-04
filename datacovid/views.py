from django.shortcuts import render, redirect
from .models import DataCovid
from .forms import dataform

# Create your views here.
def datacovid(request):
    data = DataCovid.objects.all()
    response = {'data': data}
    return render(request, 'datacovid.html', response)

def formdata(request):
    add_data = dataform(request.POST or None)
    if (add_data.is_valid() and request.method == 'POST'):
        add_data.save()
        return redirect('/data-covid')
    response = {'formdata': add_data}
    return render(request, 'datacovid_form.html', response)
