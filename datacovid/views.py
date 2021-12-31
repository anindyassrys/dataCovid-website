from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import DataCovid
from .forms import dataform
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def datacovid(request):
    data = DataCovid.objects.all()
    three_data = data[:3]
    response = {'data': data,
    'three_data' : three_data
    }
    return render(request, 'datacovid.html', response)

@login_required(login_url='/admin/login/')
def formdata(request):
    add_data = dataform(request.POST or None)
    if (add_data.is_valid() and request.method == 'POST'):
        add_data.save()
        return redirect('/data-covid')
    response = {'formdata': add_data}
    return render(request, 'datacovid_form.html', response)

def load_more(request):
    offset = int(request.POST.get('offset', 0))
    limit = 3
    posts = DataCovid.objects.all()[offset:limit+offset]
    totalData = DataCovid.objects.count()
    data = {}
    posts_json = serializers.serialize('json', posts)
    return JsonResponse(data={
        'posts': posts_json,
        'totalResult': totalData
    })

@csrf_exempt
def get_content(request):
    res = []
    content = DataCovid.objects.all()
    for i in content:
        dict = {
            "daerah" : i.daerah,
            "positif" : i.positif
        }
        res.append(dict)
    data = json.dumps(res)
    print(data) 
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def post_content(request):
    data = json.loads(request.body)
    form = dataform(data)
    form.save()

    response = HttpResponse('success')
    response.status_code = 200
    return response
