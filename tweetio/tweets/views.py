from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from tweets.models import Tweet
from django.contrib.auth.decorators import login_required

def splash(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
	    return render(request, "splash.html", {})

def home(request):
    tweets = Tweet.objects.all()
    return render(request, "home.html", {"tweets": tweets})

def profile(request):
    return render(request, "profile.html", {})

def self(request):
    # account = Account.objects.get(id=request.GET['id'])
    # tweets = Tweet.objects.filter(author=request.user)
    if request.method == 'POST':
        body = request.POST["body"]
        Tweet.objects.create(body=body)
    tweets = Tweet.objects.all()
    return render(request, "self.html", {"tweets": tweets})

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
    username = request.POST["username"]
    password = password = request.POST["password"]
    email = email = request.POST["email"]
    User.objects.create(username=username, password=password, email=email)
    # location = request.POST.get("location")
    # bio = request.POST.get("bio")
    # Account.objects.create(user, location, bio)

    # accounts = Account.objects.all()
    return redirect('/register-complete')
    # return render(request, "register.html", {"accounts": accounts})
    # return render(request, "register.html", {"users": users})

# posts

def delete_tweet(request):
    tweet = Tweet.objects.get(id=request.GET.get('id'))
    tweet.delete()