from django import forms
from .models import MembershipApplication


class MembershipApplicationForm(forms.ModelForm):

    class Meta:
        model  = MembershipApplication
        fields = [
            'full_name',
            'email',
            'phone',
            'address',
            'country',
            'occupation',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+1 000 000 0000',
                'class': 'form-input',
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Enter your full address',
                'class': 'form-input form-textarea',
                'rows': 3,
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Enter your country',
                'class': 'form-input',
            }),
            'occupation': forms.TextInput(attrs={
                'placeholder': 'Enter your occupation',
                'class': 'form-input',
            }),
        }
        labels = {
            'full_name'  : 'Full Name',
            'email'      : 'Email Address',
            'phone'      : 'Phone Number',
            'address'    : 'Address',
            'country'    : 'Country',
            'occupation' : 'Occupation',
        }