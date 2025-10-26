from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
# Create your views here.

def micros_home(request):
    return render(request, 'micros/micros-home.html', {})

@login_required
def Bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, f"Booking Successfully created for {booking.user.username} at {booking.booking_date} !!")
            return redirect('micros:ticket_url')
    else:
        form = BookingForm()
    return render(request, 'micros/booking.html', {"bookingform": form})

def Communities(request):
    projects = Project.objects.all()
    return render(request, 'micros/community.html', {"projects": projects})

def Credits(request):
    return render(request, 'micros/credits.html', {})

def Tickets(request):
    booking = Booking.objects.filter(user=request.user).last()
    return render(request, 'micros/ticket.html', {"booking": booking})

@login_required
def Reputations(request):
    if request.method == 'POST':
        form = ReputationForm(request.POST)
        if form.is_valid():
            reputation = form.save(commit=False)
            reputation.user = request.user
            reputation.save()
            messages.success(request, f"New Testimonial added !!")
            return redirect('profile')
    else:
        form = ReputationForm()
    return render(request, 'micros/reputation.html', {"reputationform": form})


def CreateCommunities(request):
    comm_form = CommunityForm(prefix="community")
    proj_form = ProjectForm(prefix="project")
    if request.method == 'POST':
        if "community-submit" in request.POST:
            comm_form = CommunityForm(request.POST, prefix="community")
            if comm_form.is_valid():
                community = comm_form.save()
                messages.success(request, f"New Community Successfully created : {community.name}!!")
                return redirect('micros:community_url')
        elif "project-submit" in request.POST:
            proj_form = ProjectForm(request.POST, prefix="project")
            if proj_form.is_valid():
                project = proj_form.save()
                messages.success(request, f"New Project Successfully created : {project.name}!!")
                return redirect('micros:community_url')
    return render(request, 'micros/create_community.html', {"communityform": comm_form, "projectform": proj_form})