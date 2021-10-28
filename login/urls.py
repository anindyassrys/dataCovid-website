from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_account, name='login'),
    path('logout/', views.logout_account, name='logout')
]