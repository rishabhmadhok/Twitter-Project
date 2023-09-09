from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    tweet_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    likers = models.ManyToManyField(User,related_name='likers')
    author = models.ForeignKey(User, on_delete = models.CASCADE)


class Hashtag(models.Model):
    hashtag_text = models.CharField(max_length = 200)
    tweets = models.ManyToManyField(Tweet)
     