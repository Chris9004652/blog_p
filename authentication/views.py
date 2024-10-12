# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login , logout
from django.views import View
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'authentication/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('blogg:home')  # Ensure this URL name is correct
        return render(request, 'authentication/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'authentication/login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blogg:home')  # Ensure this URL name is correct
        return render(request, 'authentication/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)  # Log the user out
        return redirect('blogg:home') 