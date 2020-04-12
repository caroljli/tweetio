from django.shortcuts import render

def splash(request):
	return render(request, "splash.html", {})

def home(request):
	return render(request, "home.html", {})

def login(request):
    return render(request, "login.html", {})

def register(request):
    return render(request, "register.html", {})

def profile(request):
    return render(request, "profile.html", {})

def self(request):
    return render(request, "self.html", {})

def hashtag(request):
    return render(request, "hashtag.html", {})

def register_complete(request):
    return render(request, "register-complete.html", {})