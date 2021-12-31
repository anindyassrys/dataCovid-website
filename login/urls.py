from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
	path('register', views.regisPageDesktop, name="register"),
	path('login', views.loginPageDesktop, name="login"),  
	path('logout', views.logoutUser, name="logout"),
	path('auth-login', views.loginPage),
	path('auth-register', views.regisPage)
]