from django import forms

from .models import *
from django.utils import timezone

# forms
class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time']
        
        widgets = {
            # 1. Use the calendar widget for the date
            'booking_date': DateInput(
                attrs={
                    'class': 'form-input' # For your CSS
                }
            ),
        }


class ReputationForm(forms.ModelForm):
    class Meta:
        model = Reputation
        fields = '__all__'

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = '__all__'

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'