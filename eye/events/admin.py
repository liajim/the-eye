from django.contrib import admin

# Register your models here.
from events.models import EventType


class EventTypeAdmin(admin.ModelAdmin):
    """Class for EventType admin allow to add the validation"""
    readonly_fields = ['category', 'name']

    def has_add_permission(self, request, obj=None):
        """Do not allow creation"""
        return False

    def has_delete_permission(self, request, obj=None):
        """Do not allow deletion"""
        return False


admin.site.register(EventType, EventTypeAdmin)
