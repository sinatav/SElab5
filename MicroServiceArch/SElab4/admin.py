from django.contrib import admin

from MicroServiceArch.SElab4.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
