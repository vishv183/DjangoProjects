from django.contrib import admin

from Profile.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from Profile.models import OTPDevice
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView




# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone_number', 'address', 'is_verified', 'otp')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions',
         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_portal_user')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OTPDevice)
