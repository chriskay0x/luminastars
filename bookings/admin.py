from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display  = ('client_name', 'celebrity', 'event_type', 'event_date', 'status', 'created_at')
    list_filter   = ('status', 'event_type', 'celebrity')
    search_fields = ('client_name', 'client_email', 'company', 'celebrity__name')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    ordering      = ('-created_at',)
    fieldsets = (
        ('Celebrity', {
            'fields': ('celebrity',)
        }),
        ('Client Details', {
            'fields': ('client_name', 'client_email', 'client_phone', 'company')
        }),
        ('Event Details', {
            'fields': ('event_type', 'event_date', 'event_location', 'event_description', 'budget')
        }),
        ('Internal', {
            'fields': ('status', 'notes', 'created_at', 'updated_at')
        }),
    )