from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User
from apps.users.forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "avatar", "status_online", "wins", "losses", "created_at", "updated_at"]
    list_filter = ["status_online"]
    fieldsets = [
        (None, {"fields": ["avatar", "status_online", "wins", "losses", "created_at", "updated_at"]})
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []
    readonly_fields = ("created_at", "updated_at")

admin.site.register(User, UserAdmin)
