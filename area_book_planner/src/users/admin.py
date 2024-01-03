from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # You can customize the list_display, search_fields, etc.
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
