from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    bio = models.TextField()
    time = models.DateTimeField(auto_now=True, null=True)

class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now=True, null=True)
    body = models.TextField(null=True)
    class Meta:
        ordering = ['-time']
    
    def get_username(self):
        return self.author.username
    
    def get_name(self):
        if self.profile is not None:
            return self.profile.name
        else:
            return "user"

class Like(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now=True, null=True)

class Hashtag(models.Model):
    pass