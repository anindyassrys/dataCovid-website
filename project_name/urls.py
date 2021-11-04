"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import diskusi.urls as diskusi_urls
from django.urls import include, path, re_path
from home.views import index as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rumah-sakit-rujukan/', include('rujukan.urls')),
    path('kewaspadaan', include('kewaspadaan.urls')),
    path('home', include('home.urls')),
    path('diskusi/', include(diskusi_urls)),
    path('data-covid/', include('datacovid.urls')),
    path('vaksinasi/', include('vaksinasi.urls')),
    path('', include('login.urls', 'login')),
    re_path(r'^$', home, name='home'),
]
