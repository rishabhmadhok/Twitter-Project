from django.contrib import admin

# Register your models here.
from .models import Tweet, Hashtag

admin.site.register(Tweet)
admin.site.register(Hashtag)