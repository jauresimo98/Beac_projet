 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView


def login_connexion(request):
    if request.method == "POST":
        username = request.POST['nom']
        pwd = request.POST['pwd']
        print('le nom est :',username)
        user = authenticate(username=username,password= pwd)
        if user is not None:
            print("utilisateur existant")
            return redirect('home')
        else:
            messages.error(request, "erreur t'authentification ")
            return render(request, 'users/connexion.html')
    return render(request,'users/connexion.html')


def login_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username,password= pwd)
            if user is not None:
                login(request,user)
                print(user.is_superuser)
                return redirect('home')
            else:
                messages.error(request, "erreur t'authentification ")
                print('pqs de permission')
                return render(request, 'users/login.html',{'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'is_invalid' 
            return render(request, 'users/login.html',{'form':form})


    else:
        form =LoginForm()
        return  render(request,'users/login.html',{'form':form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = User.objects.create_user(username= username, password= pwd)
            if user is not None:
                return redirect('login_login')
            else:
                messages.error(request, 'creation de compte échouée')
                render(request,'users/register.html',{'form':form})
        else:
            return render(request, 'users/register.html',{'form':form})
    form = RegisterForm()
    return render(request,'users/register.html',{'form':form}) 

def logout_block(request):
    logout(request)
    return redirect('login_login')

