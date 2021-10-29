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
from django.urls import include, path
from diskusi import urls as diskusi_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('diskusi/', include(diskusi_urls)),
    path('rumah-sakit-rujukan/', include('rujukan.urls')),
    path('main', include('main.urls')),
    path('kewaspadaan', include('kewaspadaan.urls')),
    path('home', include('Home.urls')),
    path('data-covid', include('datacovid.urls')),
    path('', include('login.urls', 'login'))
]
