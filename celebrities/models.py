from django.db import models
from django.utils.text import slugify


class Celebrity(models.Model):

    CATEGORY_CHOICES = [
        ('actor',      'Actor / Actress'),
        ('musician',   'Musician'),
        ('athlete',    'Athlete'),
        ('influencer', 'Influencer'),
        ('presenter',  'TV Presenter'),
        ('comedian',   'Comedian'),
        ('other',      'Other'),
    ]

    STATUS_CHOICES = [
        ('available',   'Available'),
        ('limited',     'Limited Availability'),
        ('unavailable', 'Unavailable'),
    ]

    # Core fields
    name        = models.CharField(max_length=150)
    slug        = models.SlugField(max_length=160, unique=True, blank=True)
    role        = models.CharField(max_length=120, help_text="e.g. Actress & Producer")
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='actor')
    bio         = models.TextField()
    photo       = models.ImageField(upload_to='celebrities/')

    # Availability
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")

    # Social & contact
    instagram   = models.URLField(blank=True)
    twitter     = models.URLField(blank=True)
    website     = models.URLField(blank=True)

    # Meta
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Celebrities'
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def get_related(self):
        return Celebrity.objects.exclude(id=self.id).filter(
            category=self.category
        )[:3] or Celebrity.objects.exclude(id=self.id)[:3]