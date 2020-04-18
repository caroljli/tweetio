from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from tweets.models import Tweet, Account, Like, Hashtag
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def splash(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
	    return render(request, "splash.html", {})

def home(request):
    user = request.user
    tweets = Tweet.objects.all()
    accounts = Account.objects.all()
    return render(request, "home.html", {"tweets": tweets, "accounts": accounts, "user": user})

def profile(request, username=None):
    if User.objects.get(username=username):
        user = User.objects.get(username=username)
        account = Account.objects.get(user=user)
        tweets = Tweet.objects.filter(author=user)
        return render(request, "profile.html", {"user": user, "account": account, "tweets": tweets})
    else:
        return render("user not found")

def self(request):
    account = Account.objects.filter(user=request.user)
    tweets = Tweet.objects.filter(author=request.user)
    likes = Like.objects.filter(user=request.user)
    return render(request, "self.html", {"tweets": tweets, "account": account, "likes": likes})

def hashtag(request, hashtag=None):
    curr_hashtag = Hashtag.objects.get(content=hashtag)
    tweets = Tweet.objects.filter(hashtags__id=curr_hashtag.id)
    return render(request, "hashtag.html", {"tweets": tweets, "hashtag": curr_hashtag})

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
        Like.objects.all().delete()
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
    tweet = Tweet.objects.get(id=request.POST.get('id'))
    tweet.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def like_clicked(request):
    if 'like' in request.POST:
        post = Tweet.objects.get(id=request.POST.get('like'))
        post.likes.add(request.user)
        account = Account.objects.get(user=request.user)
        new_like, created = Like.objects.get_or_create(user=request.user, profile=account, post=post)
    else:
        post = Tweet.objects.get(id=request.POST.get('dislike'))
        post.likes.remove(request.user)
        Like.objects.filter(user=request.user, post=post).delete()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def newpost(request):
    if request.method == 'POST':
        body = request.POST["body"]
        tweet = Tweet.objects.create(body=body, author=request.user, profile=Account.objects.get(user=request.user))

        post_body = tweet.body.split(" ")
        for n, word in enumerate(post_body):
            if '#' in word:
                word = word[1:]
                if not Hashtag.objects.filter(content=word).exists():
                    hashtag = Hashtag.objects.create(content=word)
                else:
                    hashtag = Hashtag.objects.get(content=word)
                tweet.hashtags.add(hashtag)
                post_body[n] = '<a href="' + '/.' + '/hashtag/' + word + '">#' + word + '</a>'

        post_body_str = " ".join(post_body)
        setattr(tweet, 'body', post_body_str)
        tweet.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
