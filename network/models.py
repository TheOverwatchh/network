from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Posts(models.Model):
    creator = models.CharField(max_length=20, default="UNKNOWN")
    timestamp = models.CharField(max_length=50, default="UNKNOWN")
    content = models.CharField(max_length=244, default="UNKNOWN", primary_key=True)
    like = models.BooleanField(default="false")
    
    def __str__(self):
        return self.content