from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
    )
    list_filter = (
        'is_staff', 'is_superuser', 
        'is_active',
    )
    ordering = (
        "last_name",
        "first_name",
    )
    list_per_page = 25
