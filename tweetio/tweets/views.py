from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from tweets.models import Account

def splash(request):
	return render(request, "splash.html", {})

def home(request):
    tweets = Tweet.objects.all()
    return render(request, "home.html", {"tweets": tweet})

def profile(request):
    return render(request, "profile.html", {})

def self(request):
    account = Account.objects.get(id=request.GET['id'])
    tweets = Tweet.objects.filter(author=request.user)
    return render(request, "self.html", {"account": account, "tweets": tweets})

def hashtag(request):
    return render(request, "hashtag.html", {})

def register_complete(request):
    return render(request, "register-complete.html", {})

# USER AUTHENTICATION

# redirects to self
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/self")
        else:
            return render(request, "login.html", {})

def logout_(request):
    logout(request)
    return redirect("/")

def register(request):
    user = User.objects.create_user(username=request.POST['username'],
                                    email=request.POST['email'],
                                    password=request.POST['password'])
    return redirect('/register-complete')

def delete_tweet(reqest):
    tweet = Tweet.objects.get(id=request.GET['id'])
    tweet.delete()