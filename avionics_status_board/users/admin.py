from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username', 'first_name', 'last_name', 'bems_id', 'email', 
        'last_login', 'is_lead', 'is_technician', 'is_admin'
    )
    list_filter = (
        'role', 'is_staff', 'is_superuser'
    )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'bems_id')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'bems_id')}),
        ('Additional Info', {'fields': ('job_title', 'role', 'location', 'profile_pic', 'shift')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'bems_id', 'job_title', 'role', 'location', 'profile_pic', 'shift', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
