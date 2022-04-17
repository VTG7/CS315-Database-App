# Create your views here.
from email.policy import HTTP
from pickle import NONE
from re import template
from django.shortcuts import get_object_or_404, render, redirect # !redirect added

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator #!
from . models import Song, Profile
from . forms import searchForm
from django.db.models import Q
from itertools import chain
from collections import OrderedDict

def index(request): #!
    paginator = Paginator(Song.objects.filter(title__contains='title'),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "taansen/index.html", {"page_obj":page_obj})

def playSong(request, title):
    user = Profile.objects.get(user=request.user)
    song_list2 = Song.objects.filter(title__exact=title)
    song_list1 = user.liked_songs.all()
    song_list = (song_list1 | song_list2)
    result = list(chain(song_list2, song_list1))
    result = list(OrderedDict.fromkeys(result))
    #song_list = song_list1.union(song_list2)
    paginator = Paginator(result,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "taansen/index.html", {"page_obj":page_obj})
    

class SignUpView(generic.CreateView):   # For Signup Page
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

def homeView(request):  # For home page, after login
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            title_selector = form.cleaned_data['Selector']
            artist = form.cleaned_data['artist']
            artist_selector = form.cleaned_data['Selector2']
            actor = form.cleaned_data['actor']
            actor_selector = form.cleaned_data['Selector3']
            genre = form.cleaned_data['genre']
            genre_selector = form.cleaned_data['Selector4']
            lyrics = form.cleaned_data['lyrics']
            #object_list = Song.objects.filter(Q())                    
            #object_list = Song.objects.filter(lyrics__contains = lyrics).distinct() 
            object_list = Song.objects.all() 
            if title_selector==True and title != '':
                object_list = object_list.exclude(title__contains = title)
                title = ''             
            if artist_selector==True and artist != '':
                object_list = object_list.exclude(artist__name__contains = artist)
                artist = ''  
            if actor_selector==True and actor != '':
                object_list = object_list.exclude(movie_album__actor__name__contains = actor) 
                actor = '' 
            if genre_selector==True and genre != '' :
                object_list = object_list.exclude(genre__contains = genre)
                genre = ''  
            object_list = object_list.filter(title__contains=title , artist__name__contains=artist ,movie_album__actor__name__contains = actor,genre__contains = genre, lyrics__contains = lyrics).distinct() # query with all fields selected as 'with' and not null.
            return render(request, 'taansen/search_results.html',{'object_list':object_list})
    else :
        form = searchForm()

    return render(request, 'taansen/home.html', {'form':form})

#! add @login required signal ??
def likeView(request, pk):
    song = get_object_or_404(Song, id = request.POST.get('song_id'))
    user = Profile.objects.get(user=request.user)
    user.liked_songs.add(song)
    return HttpResponseRedirect(reverse('taansen:play_song', args=[str(song.title)]))


