from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from tweets.models import Tweet, Account, Like
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def splash(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
	    return render(request, "splash.html", {})

def home(request):
    tweets = Tweet.objects.all()
    accounts = Account.objects.all()
    return render(request, "home.html", {"tweets": tweets, "accounts": accounts})

def profile(request, username=None):
    if User.objects.get(username=username):
        user = User.objects.get(username=username)
        account = Account.objects.filter(user=user)
        tweets = Tweet.objects.filter(author=user)
        return render(request, "profile.html", {
            "user": user, "account": account, "tweets": tweets
        })
    else:
        return render("user not found")

def self(request):
    account = Account.objects.filter(user=request.user)
    tweets = Tweet.objects.filter(author=request.user)
    likes = Like.objects.filter(profile=request.user)
    return render(request, "self.html", {"tweets": tweets, "account": account})

def hashtag(request):
    return render(request, "hashtag.html", {})

def register_complete(request):
    return render(request, "register-complete.html", {})

def login(request):
    return render(request, "login.html", {})

def register(request):
    return render(request, "register.html", {})

# user authentication

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect("/home")
    else:
        return redirect("/login")

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")

def register_view(request):
    name = request.POST["name"]
    username = request.POST["username"]
    password = password = request.POST["password"]
    email = request.POST["email"]
    location = request.POST["location"]
    bio = request.POST["bio"]
    user = User.objects.create(username=username, password=password, email=email)
    user.set_password(password)
    user.save()
    Account.objects.create(user=user, name=name, location=location, bio=bio)
    return redirect('/register-complete')

# posts

def delete_tweet(request):
    tweet = Tweet.objects.get(id=request.GET.get('id'))
    tweet.delete()

def like_clicked(request, post_id):
    if request.method == 'POST':
        if request.user.is_authenticated():
            post = Tweet.objects.get(id=post_id)
            if not already_liked_post(request.user, id):
                Like.objects.create(user=request.user, post=post)
            else:
                Like.objects.filter(user=request.user, post=post).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def already_liked_post(user, post_id):
    post = Tweet.objects.get(id=post_id)
    return Like.objects.filer(user=user, post=post).exists()

def newpost(request):
    if request.method == 'POST':
        body = request.POST["body"]
        Tweet.objects.create(body=body, author=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
