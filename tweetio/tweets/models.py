from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# account class extends user class
# class Account(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     bio = models.TextField()

    # username = models.CharField(
    #     'username',
    #     max_length=50,
    #     unique=True,
    #     help_text='required. 50 characters or fewer. letters, digits and @/./+/-/_ only.',
    #     error_messages={
    #         'unique': "A user with that username already exists.",
    #     },
    # )

    # email = models.EmailField(
    #     unique=True, 
    #     blank=False,
    #     error_messages={
    #         'unique': "A user with that email already exists.",
    #     },
    # )

    # location = models.CharField(max_length=100)
    # bio = models.TextField(blank=False)

    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["username", "email"]

class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    time = models.DateTimeField(auto_now=True, null=True)
    body = models.TextField(null=True)
    liked = False

class Hashtag(models.Model):
    pass