from django.urls import path
from . import views

app_name = 'datacovid'

urlpatterns = [
    path('', views.datacovid, name='datacovid'),
    path('formdata', views.formdata, name='formdata'),
    path('load-more', views.load_more, name='load-more'),
    path('get_content', views.get_content, name='get_content'),
    path('post_content', views.post_content, name='post_content')
]