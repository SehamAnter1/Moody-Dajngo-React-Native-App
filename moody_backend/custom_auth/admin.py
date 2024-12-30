from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_verified', 'is_staff', 'date_joined')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'otp')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verified')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'otp', 'is_verified'),
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)
