from django.contrib import admin
from .models import Celebrity


@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display    = ('name', 'role', 'category', 'status', 'is_featured', 'created_at')
    list_filter     = ('category', 'status', 'is_featured')
    search_fields   = ('name', 'role', 'bio')
    prepopulated_fields = {'slug': ('name',)}
    list_editable   = ('status', 'is_featured')
    ordering        = ('-is_featured', 'name')
    fieldsets = (
        ('Profile', {
            'fields': ('name', 'slug', 'role', 'category', 'photo', 'bio')
        }),
        ('Availability', {
            'fields': ('status', 'is_featured')
        }),
        ('Social & Web', {
            'fields': ('instagram', 'twitter', 'website'),
            'classes': ('collapse',)
        }),
    )