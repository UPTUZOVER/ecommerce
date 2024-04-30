from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'last_login', 'is_admin', 'is_staff', 'is_active', 'is_superuser']
    list_filter = ['is_admin', 'is_staff', 'is_active', 'is_superuser']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = [
        (None, {'fields': ['username', 'email', 'password']}),
        ('Personal Info', {'fields': ['first_name', 'last_name', 'phone_number']}),
        ('Permissions', {'fields': ['is_admin', 'is_staff', 'is_active', 'is_superuser']}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser'],
        }),
    ]


admin.site.register(Account, AccountAdmin)