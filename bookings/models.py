from django.db import models

# Create your models here.
from django.db import models
from celebrities.models import Celebrity


class Booking(models.Model):

    EVENT_TYPE_CHOICES = [
        ('corporate',  'Corporate Event'),
        ('private',    'Private Party'),
        ('wedding',    'Wedding'),
        ('concert',    'Concert / Performance'),
        ('brand',      'Brand Campaign'),
        ('appearance', 'Public Appearance'),
        ('virtual',    'Virtual Event'),
        ('other',      'Other'),
    ]

    STATUS_CHOICES = [
        ('pending',   'Pending Review'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    # Who's being booked
    celebrity    = models.ForeignKey(Celebrity, on_delete=models.CASCADE, related_name='bookings')

    # Client details
    client_name  = models.CharField(max_length=150)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=30, blank=True)
    company      = models.CharField(max_length=150, blank=True)

    # Event details
    event_type   = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    event_date   = models.DateField()
    event_location = models.CharField(max_length=200)
    event_description = models.TextField(help_text="Describe your event and requirements")
    budget       = models.CharField(max_length=100, blank=True, help_text="Approximate budget range")

    # Internal
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes        = models.TextField(blank=True, help_text="Internal team notes")
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} — {self.celebrity.name} ({self.event_date})"