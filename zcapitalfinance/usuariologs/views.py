# from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.shortcuts import render, redirect


#Menu
def menu(request):
    return render(request, 'usuariologs/menu.html')

#Login
def login(request):
    return render(request, 'usuariologs/login.html')

#Logout
def custom_logout(request):
    logout(request)

    return redirect('/')