from django.contrib import admin
from django.urls import path

# added lines
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

#app name
app_name = 'micros'

urlpatterns = [
    path('', views.micros_home, name="micros_home_url"),
    path('booking/', views.Bookings, name="booking_url"),
    path('credit/', views.Credits, name="credit_url"),
    path('community/', views.Communities, name="community_url"),
    path('create-community/', views.CreateCommunities, name="create-community_url"),
    path('reputation/', views.Reputations, name="reputation_url"),
    path('ticket/', views.Tickets, name="ticket_url"),
]