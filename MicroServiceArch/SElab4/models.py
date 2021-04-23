from django.db import models


# we have two user roles , client and admin, and we have a token field which is what is traded between
# the different users

class User(models.Model):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    isAdmin = models.BooleanField(default=False)
    token = models.CharField(max_length=250, default="")
    token_time = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    _id = models.AutoField(primary_key=True)
