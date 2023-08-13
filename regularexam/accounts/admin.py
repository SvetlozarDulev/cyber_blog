from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "years_experience",
        "is_staff",
    ]
    list_filter = ["is_staff","is_superuser", "groups"]
    search_fields = ["email",]
    ordering = ("username",)


    # Extend the existing 'fieldsets' attribute from 'UserAdmin' to add a new field ('years_experience')
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("years_experience",)}),)

    # Extend the existing 'add_fieldsets' attribute from 'UserAdmin' to add the same new field ('years_experience')
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("years_experience",)}),)

# Register the 'CustomUser' model with the custom admin class 'CustomUserAdmin'
admin.site.register(CustomUser, CustomUserAdmin)