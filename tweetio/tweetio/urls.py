"""tweetio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from tweets.views import splash, home, login,register, login_view, register_view, profile, self, hashtag, register_complete, logout_view, delete_tweet, newpost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name='splash'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('login_view/', login_view, name='login_view'),
    path('register_view/', register_view, name='register_view'),
    path('self/', self, name='self'),
    path('hashtag/', hashtag, name='hashtag'),
    path('register-complete/', register_complete, name="register-complete"),
    path('logout/', logout_view, name="logout"),
    path('delete_tweet/', delete_tweet, name='delete_tweet'),
    path('newpost/', newpost, name="newpost"),
    path('profile/<slug:username>', profile, name="profile"),
]
