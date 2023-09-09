from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .models import Hashtag
from django.db import models
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
@login_required(login_url='/twitter/login')
def posttweet(request):
    author = request.user
    text = request.POST['tweet_text']
    tweet = Tweet(tweet_text=text, author=author)
    tweet.save()

    words = text.split()
    print(words)
    for i in words:
        if i[0] == '#':
            try:
                hashtag = Hashtag.objects.get(hashtag_text=i)
            except Hashtag.DoesNotExist:
                hashtag = Hashtag(hashtag_text=i)
                hashtag.save()

            # associate this hashtag  with the tweet 
            # add tweet to hashtag.tweets
            hashtag.tweets.add(tweet)

            

            
            

    return redirect('homepage')

def signup(request):
    
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username, '', password)
            user.save()
            login(request, user)
            return redirect('homepage')

        return render(request, 'twitter/signup.html')
    except:
           return render(request, 'twitter/signup.html', {'error_message': 'Invalid username'})



def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'twitter/login.html', {'error_message': 'Invalid login'})
    
    return render(request, 'twitter/login.html')

@login_required(login_url='/twitter/login')
def homepage(request):
    tweets = Tweet.objects.all()
    context = {'tweets':tweets}
    return render(request,'twitter/homepage.html',context)

@login_required(login_url='/twitter/login')
def unlike(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.likers.remove(request.user)
    
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='/twitter/login')
def liketweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.likers.add(request.user)
    
    return redirect(request.META['HTTP_REFERER'])

def profilepage(request,username):
    user = User.objects.get(username=username)
    tweets = Tweet.objects.filter(author = user)
    context = {'tweets':tweets}
    
    
    return render(request,'twitter/profilepage.html', context)

def searchhashtags(request):
    thehashtag = request.GET['hashtag_text']
    return redirect('hashtagpage', tag=thehashtag)

def hashtagpage(request, tag):
    hashtag = Hashtag.objects.get(hashtag_text = tag)
    context = {'tweets':hashtag.tweets.all()}
    return render(request,'twitter/hashtagpage.html',context)

def my_logout(request):
    logout(request)
    return redirect('my_login')


