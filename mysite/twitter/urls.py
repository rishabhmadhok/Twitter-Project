from django.urls import path
from.import views

urlpatterns = [
    path('home', views.homepage, name='homepage'),
    path('posttweet',views.posttweet,name = 'posttweet'),
    path('login',views.my_login,name = 'my_login'),
    path('signup',views.signup,name = 'signup'),
    path('like/<int:tweet_id>', views.liketweet, name='like'),
    path('unlike/<int:tweet_id>', views.unlike, name='unlike'),
    path('profilepage/<str:username>',views.profilepage,name = 'profilepage'),
    path('hashtagpage/<str:tag>',views.hashtagpage,name = 'hashtagpage'),
    path('my_logout',views.my_logout,name = 'my_logout'),
    path('searchhashtags',views.searchhashtags,name = 'searchhashtags'),
]