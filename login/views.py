from django.shortcuts import render, redirect 
from django.http import HttpResponse, JsonResponse, response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from django.contrib import messages



# Create your views here.
from .models import *
from .forms import createUserForm


def regisPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = createUserForm()
		if request.method == 'POST':
			form = createUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login:login')
			

		context = {'form':form}
		return render(request, 'register_acc.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username or password is incorrect')

		context = {}
		return render(request, 'login_acc.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login:login')

# def userValidation(request):
#     User = get_user_model()
#     userA = User.objects.all()

#     if request():
#         username = request.POST.get("username")
#         for user in userA:
#             if username == user.username:
#                 return JsonResponse({"error": "Sorry, this username is already taken"}, status=400)
#     return JsonResponse({"success": "Username available"}, status=200)