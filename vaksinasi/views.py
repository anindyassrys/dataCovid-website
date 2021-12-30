from django.shortcuts import render
from .models import Kategori
from django.http.response import HttpResponse
from django.core import serializers
from datetime import date
import random

def vaksinasi(request):

    try:
        kategoris = Kategori.objects.all().values()
    except kategoris.DoesNotExist:
        kategoris = None
    # kategoris = Kategori.objects.all().values()

    update()

    context = {'kategoris': kategoris}
    return render(request, 'vaksinasi.html', context)

def kategori(request):
    update()
    data = serializers.serialize('json', Kategori.objects.all())
    return HttpResponse(data, content_type="application/json")

def update():
    """
    method ini bertujuan untuk mengupdate value telah_vaksin_dosis_1, telah_vaksin_dosis_2, dan per_tanggal dari setiap kategori di database
    value dari telah_vaksin_dosis_1, telah_vaksin_dosis_2 bergantung pada berapa hari value dari mereka tidak diupdate
    """
    today = date.today()
    random_number_dosis_1 = random.randint(25,75)/10000 # 0.25% - 0.75%
    random_number_dosis_2 = random.randint(25,75)/10000
    for i in range(1,7):    # iterasi untuk setiap models Kategori (id = 1 sampai id = 6)
        kategori = Kategori.objects.get(id = i)
        day_gap = today - kategori.per_tanggal  # selisih hari saat update terakhir

        if day_gap.days > 0:
            """
            asumsi pertumbuhan vaksinasi adalah (0.25% - 0.75%) dari target vaksinasi / hari
            dengan kata lain data ini tidak sesuai dengan data sebenarnya
            """
            kategori.telah_vaksin_dosis_1 += round(day_gap.days * random_number_dosis_1 * kategori.target_vaksin)
            kategori.telah_vaksin_dosis_2 += round(day_gap.days * random_number_dosis_2 * kategori.target_vaksin)
            kategori.per_tanggal = today    # set tanggal update terakhir

        if kategori.telah_vaksin_dosis_1 > kategori.target_vaksin:
            kategori.telah_vaksin_dosis_1 = kategori.target_vaksin

        if kategori.telah_vaksin_dosis_2 > kategori.target_vaksin:
            kategori.telah_vaksin_dosis_2 = kategori.target_vaksin

        kategori.save() # save