from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model  = ContactMessage
        fields = ['full_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+1 000 000 0000',
                'class': 'form-input',
            }),
            'subject': forms.Select(attrs={
                'class': 'form-input form-select',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell us how we can help you...',
                'class': 'form-input form-textarea',
                'rows': 6,
            }),
        }
        labels = {
            'full_name' : 'Full Name',
            'email'     : 'Email Address',
            'phone'     : 'Phone Number',
            'subject'   : 'Subject',
            'message'   : 'Message',
        }