from django.contrib import admin
from .models import Work

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "type", "status", "assigned_to", "created_at")
    list_filter = ("status", "type")
