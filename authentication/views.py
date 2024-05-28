from django.shortcuts import render, redirect
from authentication.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
        
        login_form = LoginForm()
        
        if request.user.is_authenticated:
                return redirect('home')
        
        if request.method == 'POST':
                login_form = LoginForm(request.POST)
                if login_form.is_valid():
                        user = authenticate(
                                	username=login_form.cleaned_data['username'],
					password=login_form.cleaned_data['password'],
                                )
                        if user is not None:
                                login(request, user)
                                return redirect('home')
        return render(request, 'authentication/login.html', {'login_form' : login_form})

def logout_view(request):
        logout(request)
        return redirect('login')

def register(request):
        
        register_form = RegisterForm()
        
        if request.method == 'POST':
                register_form = RegisterForm(request.POST, request.FILES)
                if register_form.is_valid():
                        user = register_form.save()
                        login(request, user)
                        return redirect('home')
        
        return render(request, 'authentication/register.html', {'register_form' : register_form})

@login_required
def edit_profil(request):
        edit_form = RegisterForm(instance=request.user)
        
        if request.method == 'POST':
                edit_form = RegisterForm(request.POST, request.FILES, instance=request.user)
                if edit_form.is_valid():
                        edit_form.save()
                        return redirect('home')
        return render(request, 'authentication/edit_profil.html', {'edit_form' : edit_form})