from django.db import models


class MembershipPlan(models.Model):
    """The 3 tiers — manageable via admin."""

    TIER_CHOICES = [
        ('regular', 'Regular'),
        ('premium', 'Premium'),
        ('vip',     'VIP'),
    ]

    tier        = models.CharField(max_length=20, choices=TIER_CHOICES, unique=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    tagline     = models.CharField(max_length=120, help_text="Short description under price")
    is_featured = models.BooleanField(default=False, help_text="Highlights this plan as 'Most Popular'")
    benefits    = models.TextField(help_text="One benefit per line")

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f"{self.get_tier_display()} — ${self.price}"

    def get_benefits_list(self):
        """Returns benefits as a clean Python list."""
        return [b.strip() for b in self.benefits.splitlines() if b.strip()]


class MembershipApplication(models.Model):
    """Submitted membership applications."""

    STATUS_CHOICES = [
        ('pending',   'Pending Review'),
        ('approved',  'Approved'),
        ('rejected',  'Rejected'),
    ]

    plan        = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE, related_name='applications')
    full_name   = models.CharField(max_length=150)
    email       = models.EmailField()
    phone       = models.CharField(max_length=30)
    address     = models.TextField()
    country     = models.CharField(max_length=100)
    occupation  = models.CharField(max_length=120)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes       = models.TextField(blank=True, help_text="Internal notes")
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} — {self.plan.get_tier_display()} ({self.status})"