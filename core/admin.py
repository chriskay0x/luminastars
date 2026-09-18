from django.contrib import admin
from .models import Project, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'year', 'is_featured', 'order')
    list_filter   = ('category', 'year', 'is_featured')
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'description')
    ordering      = ('-year', 'order')
    
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ('full_name', 'email', 'subject', 'is_read', 'created_at')
    list_filter   = ('subject', 'is_read')
    search_fields = ('full_name', 'email', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    ordering      = ('-created_at',)