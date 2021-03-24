from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_active']
    list_filter = ['date_joined', 'is_staff', 'is_active']
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Additional Info',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'view_count',
                    'down_vote_count',
                    'up_vote_count',
                    'timed_penalty_date',
                    'reputation',
                    'about_me',
                    'location',
                    'website_url',
                    'link',
                ),
            },
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ['email']
    ordering = ['email']


admin.site.register(CustomUser, CustomUserAdmin)