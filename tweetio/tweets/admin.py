from django.contrib import admin
from tweets.models import Tweet, Account, Like

admin.site.register(Account)
admin.site.register(Tweet)
admin.site.register(Like)
