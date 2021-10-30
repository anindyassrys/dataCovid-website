from django.urls import path
from . import views

urlpatterns = [
    path('', views.vaksinasi, name='vaksinasi'),
    path('/kategori', views.kategori, name='kategori'),
]