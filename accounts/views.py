from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login(request):


    return render(request, 'login.html')


def change_admin_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        user =authenticate(username='admin',password=password)
        if user is not None:
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            if new_password == confirm_password :
                admin_user = User.objects.get(username='admin')
                admin_user.set_password(new_password)
                admin_user.save()
                return redirect('home')
    return render(request, 'profile.html')

