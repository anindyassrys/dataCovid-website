from django.http import response
from django.shortcuts import render
from diskusi.models import Discussion

# Create your views here.


def index(request):
    discussions = Discussion.objects.all().values()
    response = {'discussions': discussions}
    return render(request, "diskusi/index.html", response)
