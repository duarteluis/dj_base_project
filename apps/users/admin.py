from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm
from .models import ProfilUser, User


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ("email", "last_name", "first_name", "is_admin")
    list_filter = ("is_admin", "type")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal data", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_admin", "date_joined", "type")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ("email",)
    filter_horizontal = ()


class ProfilUserAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "birth_date",
    )
    list_filter = ("birth_date",)


# Now register the new UserAdmin...
admin.site.register(User, CustomUserAdmin)
admin.site.register(ProfilUser, ProfilUserAdmin)
