
from django.db import models

# we have two user roles , client and admin, and we have a token field which is what is traded between
# the different users

class User(models.Model):
    username = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    isAdmin = models.BooleanField(default=False)
    token = models.CharField(max_length=256, default="")