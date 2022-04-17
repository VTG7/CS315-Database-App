from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from .views import SignUpView, likedPage

app_name = 'taansen'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home', views.homeView, name='home'),   
    path('', views.index, name = 'index'), #! will give a useless page for now on visiting /taansen/
    path('likedSongs/', views.likedPage, name = 'likedPage'),
    path('songHistory/', views.songHistory, name = 'songHistory'),
    path('<str:title>/', views.playSong, name = 'play_song'),
    path('liked/<int:pk>', views.likeView, name = 'liked_songs'),
    path('spellcheck', views.spellCheck, name = 'spellcheck'),
    ]
