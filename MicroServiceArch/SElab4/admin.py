from django.contrib import admin

from MicroServiceArch.SElab4.models import User, Book


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
