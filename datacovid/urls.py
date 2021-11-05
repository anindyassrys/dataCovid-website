from django.urls import path
from . import views

app_name = 'datacovid'

urlpatterns = [
    path('', views.datacovid, name='datacovid'),
    path('formdata', views.formdata, name='formdata'),
    path('load-more', views.load_more, name='load-more'),
]