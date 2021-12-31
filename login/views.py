import json

from django.shortcuts import render, redirect 
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth, logout
from django.http import JsonResponse

from django.contrib import messages

# Create your views here.
from .models import *
from .forms import createUserForm

@csrf_exempt
def regisPage(request):
  form = createUserForm(json.loads(request.body))
  if form.is_valid():
    user = form.save()
    auth(request, user)
    return JsonResponse({
      "status": True,
      "message": "Register successful",
    }, status=200)
  else:
    return JsonResponse(form.errors, status=400)

# def regisPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = createUserForm()
# 		if request.method == 'POST':
# 			form = createUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, '     Account was created for ' + user)

# 				return redirect('login:login')
			

# 		context = {'form':form}
# 		return render(request, 'register_acc.html', context)


@csrf_exempt
def loginPage(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth(request, user)
            return JsonResponse({
              "status": True,
              "username": user.username,
              "message": "Successfully logged in!"
            })
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to login, account disabled."
            }, status=401)
            
    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to login, check your email or password."
        }, status=401)

# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return redirect('home')
# 			else:
# 				messages.info(request, 'Username or password is incorrect')

# 		context = {}
# 		return render(request, 'login_acc.html', context)

@csrf_exempt
def logoutUser(request):
	logout(request)
	return redirect('login:login')