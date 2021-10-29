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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('rumah-sakit-rujukan/', include('rujukan.urls')),
    path('main', include('main.urls')),
    path('kewaspadaan', include('kewaspadaan.urls')),
    path('home', include('Home.urls')),
<<<<<<< HEAD
    path('data-covid/', include('datacovid.urls')),
=======
    path('data-covid', include('datacovid.urls')),
    path('', include('login.urls', 'login'))
>>>>>>> 643e492340770d1cd45fa31357096bf93231087d
]
