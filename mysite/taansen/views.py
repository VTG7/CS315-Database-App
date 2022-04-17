# For spellcheck
import sqlite3 as db
from contextlib import closing
from nltk import trigrams
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
from . models import Song, Profile, Actor, Artist, MovieAlbum
from . forms import searchForm
from django.db.models import Q
from itertools import chain
from collections import OrderedDict

def index(request): #!
    paginator = Paginator(Song.objects.filter(title__contains='title'),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "taansen/index_alt.html", {"page_obj":page_obj})

def playSong(request, title):
    user = Profile.objects.get(user=request.user)
    song_list2 = Song.objects.filter(title__exact=title)
    song_list1 = user.liked_songs.all()
    song_list = (song_list1 | song_list2)
    result = list(chain(song_list2, song_list1))
    result = list(OrderedDict.fromkeys(result))
    #song_list = song_list1.union(song_list2)
    liked = 0
    if song_list2.first() in user.liked_songs.all():
        liked = 1
    # Adding Song History logic now:
    #user.song_history.remove(song_list2.first())  # .first used only to get the song object. Warna ek hi gaana rahega in song_list2 
    #user.song_history.add(song_list2.first()) # .first used only to get the song object. Warna ek hi gaana rahega in song_list2
    #song_list3 = user.song_history.all()
    #history = list(chain(song_list2,song_list3))
    #history = list(OrderedDict.fromkeys(history))
    #for song in history:
    #    user.song_history.add(song)
    paginator = Paginator(result,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "taansen/index_alt.html", {"page_obj":page_obj, "liked":liked})
    

class SignUpView(generic.CreateView):   # For Signup Page
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

def homeView(request):  # For home page, after login
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            with closing(db.connect(r"spellcheck.db")) as conn:
                conn.enable_load_extension(True)
                conn.load_extension("taansen/sqlite/spellfix.so")
                with closing(conn.cursor()) as cursor:
                    title = form.cleaned_data['title']
                    f_title = fetcher(cursor, title, 0)
                    title = title if len(f_title) == 0 or len(title) == 0 else f_title[0][0]
                    title_selector = form.cleaned_data['Selector']

                    artist = form.cleaned_data['artist']
                    f_artist = fetcher(cursor, artist, 4)
                    artist = artist if len(f_artist) == 0 or len(artist) == 0 else f_artist[0][0]
                    artist_selector = form.cleaned_data['Selector2']

                    actor = form.cleaned_data['actor']
                    f_actor = fetcher(cursor, actor, 3)
                    actor = actor if len(f_actor) == 0 or len(actor) == 0 else f_actor[0][0]
                    actor_selector = form.cleaned_data['Selector3']

                    genre = form.cleaned_data['genre']
                    f_genre = fetcher(cursor, genre, 1)
                    genre = genre if len(f_genre) == 0 or len(genre) == 0 else f_genre[0][0]
                    genre_selector = form.cleaned_data['Selector4']

                    lyrics = form.cleaned_data['lyrics']
                    f_lyrics = fetcher(cursor, lyrics, 2)
                    lyrics = lyrics if len(f_lyrics) == 0 or len(lyrics) == 0 else f_lyrics[0][0]

                    object_list = Song.objects.all() 
                    user = Profile.objects.get(user=request.user)
                    liked_songs = user.liked_songs.all()  
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
    liked = 0
    if song in user.liked_songs.all():
        user.liked_songs.remove(song)
    else:
        user.liked_songs.add(song)
        liked = 1
    return HttpResponseRedirect(reverse('taansen:play_song', args=[str(song.title)]))

def likedPage(request) :
    user = Profile.objects.get(user = request.user)
    object_list = user.liked_songs.all()
    return render(request, 'taansen/liked.html',{'object_list':object_list})

def songHistory(request) :
    user = Profile.objects.get(user = request.user)
    object_list = user.song_history.all().order_by()
    return render(request, 'taansen/history.html', {'object_list':object_list})

x = 1
def spellCheck(request):
    global x
    if x == 1:
        with closing(db.connect(r"spellcheck.db")) as conn:
            conn.enable_load_extension(True)
            conn.load_extension("taansen/sqlite/spellfix.so")

            with closing(conn.cursor()) as cursor:
                cursor.execute("CREATE VIRTUAL TABLE IF NOT EXISTS vocab USING spellfix1")
                cursor.execute("CREATE TABLE IF NOT EXISTS dict (word TEXT, langid INT)")
                songs = Song.objects.all()
                actors = Actor.objects.all()
                artists = Artist.objects.all()
                movies = MovieAlbum.objects.all()
                for song in songs:
                    cursor.execute("INSERT INTO dict VALUES (?, ?)", (song.title, 0)) # 0 for title
                    cursor.execute("INSERT INTO dict VALUES (?, ?)", (song.genre, 1)) # 1 for genre
                    for w in trigrams(song.lyrics.split()):
                        x = " ".join(w)
                        # print(x)
                        cursor.execute("INSERT INTO dict VALUES (?, ?)", (x, 2)) # 2 for lyrics
                for actor in actors:
                        cursor.execute("INSERT INTO dict VALUES (?, ?)", (actor.name, 3)) # 3 for actor
                for artist in artists:
                        cursor.execute("INSERT INTO dict VALUES (?, ?)", (artist.name, 4)) # 4 for artist

                cursor.execute("INSERT INTO vocab(word, langid) SELECT DISTINCT word, langid from dict")

                conn.commit()
                print(cursor.execute("SELECT DISTINCT word FROM vocab WHERE word MATCH \"Arjit Shingh\" AND langid = 4").fetchall())
    #x = 0
    return render(request, 'taansen/spellcheck.html')

def fetcher(cursor ,match, langid):
    return cursor.execute("SELECT DISTINCT word FROM vocab WHERE word MATCH \"%s\" AND langid = %s"% (match, langid)).fetchall()