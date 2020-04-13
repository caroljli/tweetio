from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from tweets.models import Account

def splash(request):
	return render(request, "splash.html", {})

def home(request):
	return render(request, "home.html", {})

def profile(request):
    return render(request, "profile.html", {})

def self(request):
    account = Account.objects.all()
    return render(request, "self.html", {"account" : account})

def hashtag(request):
    return render(request, "hashtag.html", {})

def register_complete(request):
    return render(request, "register-complete.html", {})

# USER AUTHENTICATION

# redirects to self
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/self")
    return render(request, "login.html", {})

def logout_(request):
    logout(request)
    return redirect("/")

def register(request):
    user = User.objects.create_user(username=request.POST['username'],
                                    email=request.POST['email'],
                                    password=request.POST['password'])
    return redirect('/register-complete')

def register(request):
    return render(request, "register.html", {})