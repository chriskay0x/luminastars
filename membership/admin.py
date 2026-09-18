from django.contrib import admin
from .models import MembershipPlan, MembershipApplication


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display  = ('tier', 'price', 'is_featured', 'tagline')
    list_editable = ('price', 'is_featured')
    ordering      = ('price',)


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display  = ('full_name', 'email', 'plan', 'country', 'status', 'created_at')
    list_filter   = ('status', 'plan')
    search_fields = ('full_name', 'email', 'country', 'occupation')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    ordering      = ('-created_at',)
    fieldsets = (
        ('Applicant', {
            'fields': ('full_name', 'email', 'phone', 'address', 'country', 'occupation')
        }),
        ('Membership', {
            'fields': ('plan', 'status', 'notes')
        }),
        ('Meta', {
            'fields': ('created_at',)
        }),
    )