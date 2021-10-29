from django.urls import path
from . import views

app_name = 'datacovid'

urlpatterns = [
    path('', views.datacovid, name='datacovid'),
    path('formdata', views.formdata, name='formdata'),
]