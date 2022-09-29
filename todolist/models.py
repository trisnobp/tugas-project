import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    title = models.TextField(null=True)
    description = models.TextField(null=True)