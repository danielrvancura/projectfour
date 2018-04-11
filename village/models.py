from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Child(models.Model):
    # likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.CharField(max_length=550)
    child_age = models.IntegerField()
    # parent_Name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    affliction = models.CharField(max_length=100)
    location = models.IntegerField()
    gender = models.CharField(max_length=100, default="Male")
