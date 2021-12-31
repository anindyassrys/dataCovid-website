from django.urls import path
from . import views

app_name = 'kewaspadaan'

urlpatterns = [
    path('', views.kewaspadaan, name='kewaspadaan'),
    path('add', views.add, name='addIndikator'),
    path('jsonWaspada', views.jsonWaspada, name='jsonWaspada'),
]