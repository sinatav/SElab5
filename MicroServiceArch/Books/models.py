from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    _id = models.AutoField(primary_key=True)
