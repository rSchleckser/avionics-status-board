from django.contrib import admin
from .models import Airplane

@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ("line_number", "effectivity", "customer", "delivered", "ticketed", "created_at")
    list_filter = ("line_number", "ticketed", "delivered", "effectivity")