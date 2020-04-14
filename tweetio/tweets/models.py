from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    bio = models.TextField()
    time = models.DateTimeField(auto_now=True, null=True)

    @property
    def like_count(self):
        return Like.objects.filter(user=self.user).count()
    
    def has_likes(self):
        if self.like_count > 0:
            return True
        else:
            return False

class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    # str_id = str(id)
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
    @property
    def like_count(self):
        return Like.objects.filter(post=self).count()
    
    def already_liked(self):
        if self.like_count > 0:
            return True
        else:
            return False
    
    # def save(self):
    #     new_id = self.id
    #     self.string_id = str(new_id)
    #     super(Tweet, self).save()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now=True, null=True)

    def get_username(self):
        if self is not None:
            if self.post is not None:
                return self.post.get_username
        else:
            return

    def get_post_body(self):
        if self is not None:
            if self.post is not None:
                return self.post.body
        else:
            return

class Hashtag(models.Model):
    content = models.CharField(max_length=200, null=True)
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True)