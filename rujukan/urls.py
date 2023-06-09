from django.urls import path
from . import views

app_name = 'rujukan'

urlpatterns = [
    path('', views.index, name='rujukan'),
    path('tambah', views.add, name='tambahRS'),
    path('jsonRS', views.jsonRS, name='jsonRS'),
    path('jsonWilayah', views.jsonWilayah, name='jsonWilayah'),
]
