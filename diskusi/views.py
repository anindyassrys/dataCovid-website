from django.http import response
from django.shortcuts import render
from diskusi.models import Discussion
from diskusi.forms import DiscussionForm
from django.http.response import HttpResponseRedirect

# Create your views here.


def index(request):
    discussions = Discussion.objects.all().values()
    response = {'discussions': discussions}
    return render(request, "diskusi/index.html", response)

def add_diskusi(request):
    context = {}

    form = DiscussionForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        tempForm = form.save(commit=False)

        tempForm.user = request.user
        tempForm.save()
        return HttpResponseRedirect("/diskusi")

    context['form'] = form
    return render(request, "diskusi/tambah_diskusi.html", context)