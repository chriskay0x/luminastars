from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model  = Booking
        fields = [
            'client_name',
            'client_email',
            'client_phone',
            'company',
            'event_type',
            'event_date',
            'event_location',
            'event_description',
            'budget',
        ]
        widgets = {
            'client_name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': 'form-input',
            }),
            'client_email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'class': 'form-input',
            }),
            'client_phone': forms.TextInput(attrs={
                'placeholder': '+1 000 000 0000',
                'class': 'form-input',
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'Company or organisation (optional)',
                'class': 'form-input',
            }),
            'event_type': forms.Select(attrs={
                'class': 'form-input form-select',
            }),
            'event_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input',
            }),
            'event_location': forms.TextInput(attrs={
                'placeholder': 'City, Country',
                'class': 'form-input',
            }),
            'event_description': forms.Textarea(attrs={
                'placeholder': 'Tell us about your event, requirements and expectations...',
                'class': 'form-input form-textarea',
                'rows': 5,
            }),
            'budget': forms.TextInput(attrs={
                'placeholder': 'e.g. $10,000 – $20,000',
                'class': 'form-input',
            }),
        }
        labels = {
            'client_name'       : 'Full Name',
            'client_email'      : 'Email Address',
            'client_phone'      : 'Phone Number',
            'company'           : 'Company / Organisation',
            'event_type'        : 'Event Type',
            'event_date'        : 'Event Date',
            'event_location'    : 'Event Location',
            'event_description' : 'Event Description',
            'budget'            : 'Budget Range',
        }