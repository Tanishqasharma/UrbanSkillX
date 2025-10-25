from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserSignUpForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import CustomLoginForm
from micros.models import *

def signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set new users as non-admin and non-staff
            user.is_staff = False
            user.is_superuser = False
            user.save() # Save the user to the database
            
            login(request, user) # Log the new user in automatically
            return redirect('makeportfolio') # Redirect to your home page
    else:
        form = UserSignUpForm()
    
    return render(request, 'UrbanSkillX/signup.html', {'form': form})

def home(request):
    return render(request, 'UrbanSkillX/homepage.html')

def about(request):
    return render(request, 'UrbanSkillX/aboutus.html')

def profile(request):
    reputations = Reputation.objects.all()  
    return render(request, 'UrbanSkillX/profile.html', {'reputations': reputations})

def makeportfolio(request):
    return render(request, 'UrbanSkillX/makeportfolio.html', {})

def create_acc(request):
    return render(request, 'UrbanSkillX/create_acc.html', {})