from django.contrib import admin

from MicroServiceArch.SElab4.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
