from django.db import models

## added
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    TIME_SLOTS = [
        (datetime.time(9, 0),   "9:00 AM - 10:00 AM"),
        (datetime.time(10, 0), "10:00 AM - 11:00 AM"),
        (datetime.time(11, 0), "11:00 AM - 12:00 PM"),
        (datetime.time(13, 0),  "1:00 PM - 2:00 PM"),
        (datetime.time(14, 0),  "2:00 PM - 3:00 PM"),
        (datetime.time(15, 0),  "3:00 PM - 4:00 PM"),
        (datetime.time(16, 0),  "4:00 PM - 5:00 PM"),
    ]

    booking_date = models.DateField("Booking Date")
    booking_time = models.TimeField("Booking Slot", choices=TIME_SLOTS)    
    reminder = models.BooleanField(name="Want a reminder within 24 hours", default=True)

    def __str__(self):
        return f"Booking for {self.user.username} on {self.booking_date}"
    

class Reputation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reputation')
    class starChoices(models.IntegerChoices):
        ONE = 1, "1 STAR"
        TWO = 2, "2 STAR"
        THREE = 3, "3 STAR"
        FOUR = 4, "4 STAR"
        FIVE = 5, "5 STAR"
    rating = models.PositiveSmallIntegerField(choices=starChoices)
    testimonial = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=100, blank=True, null=True)

class Credit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit')
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.amount

class Community(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='community_admin')
    members = models.ManyToManyField(User, related_name='community_member', blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="projects")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name