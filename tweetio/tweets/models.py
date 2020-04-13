from django.db import models
from django.contrib.auth.models import User

# account class extends user class
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    bio = models.TextField()

class Tweet(models.Model):
    # TODO: implement author
    time = models.DateTimeField()
    body = models.TextField()
    liked = False