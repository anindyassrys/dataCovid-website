from django.urls import path
from .views import index, add_diskusi

app_name = "diskusi"

urlpatterns = [
    path('', index, name="index"),
    path('tambah-diskusi', add_diskusi, name="form")
]