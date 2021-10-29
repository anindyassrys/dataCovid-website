from django.urls import path
from .views import index

app_name='Home'

urlpatterns= [
    path('', index, name='Home')
]