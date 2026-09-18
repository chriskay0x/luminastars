from django.db import models


class Project(models.Model):

    CATEGORY_CHOICES = [
        ('tour',        'Music Tour'),
        ('brand',       'Brand Campaign'),
        ('film',        'Film & Media'),
        ('appearance',  'Public Appearance'),
        ('event',       'Corporate Event'),
        ('other',       'Other'),
    ]

    title       = models.CharField(max_length=150)
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    year        = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image       = models.ImageField(upload_to='projects/')
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    order       = models.PositiveIntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ['-year', 'order']

    def __str__(self):
        return f"{self.title} ({self.year})"
    
    
class ContactMessage(models.Model):

    SUBJECT_CHOICES = [
        ('booking',    'Booking Enquiry'),
        ('membership', 'Membership Enquiry'),
        ('partnership','Brand Partnership'),
        ('press',      'Press & Media'),
        ('general',    'General Enquiry'),
    ]

    full_name   = models.CharField(max_length=150)
    email       = models.EmailField()
    phone       = models.CharField(max_length=30, blank=True)
    subject     = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message     = models.TextField()
    is_read     = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} — {self.get_subject_display()} ({self.created_at.strftime('%d %b %Y')})"