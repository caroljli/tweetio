from django.contrib import admin
from tweets.models import Tweet, Account, Like, Hashtag

admin.site.register(Account)
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Hashtag)
