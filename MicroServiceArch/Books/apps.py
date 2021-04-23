from django.apps import AppConfig

from MicroServiceArch import Books


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Books'
