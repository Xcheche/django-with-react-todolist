from django.contrib import admin
from .models import Todo
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'completed', 'user')
    search_fields = ('title', 'memo')
    list_filter = ('completed', 'created', 'user')
    list_display_links = ('title',)
    ordering = ('-created',)
    list_editable = ('completed',)
    fieldsets = (
        (None, {
            'fields': ('title', 'memo', 'user')
        }),
        ('Status', {
            'fields': ('completed',)
        }),
    )
    readonly_fields = ('created',)
    
