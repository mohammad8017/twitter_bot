from email.policy import default
from django.db import models



class Tweet_user(models.Model):
    username=models.CharField(max_length=150)
    user_id=models.IntegerField(default=0)
    date=models.DateTimeField(default="0000-01-01 00:00:00")
    text=models.TextField(default="")

class Tweet_hashtag(models.Model):
    hashtag=models.CharField(max_length=100)
    username=models.CharField(max_length=150)
    user_id=models.IntegerField(default=0)
    date=models.DateTimeField(default="0000-01-01 00:00:00")
    text=models.TextField(default="")


# Create your models here.
