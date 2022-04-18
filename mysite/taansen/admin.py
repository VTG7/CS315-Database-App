from django.contrib import admin
from . models import Song, MovieAlbum, Actor, Artist, Profile, Time

# Register your models here.
admin.site.register(Song)
admin.site.register(MovieAlbum)
admin.site.register(Actor)
admin.site.register(Artist)
admin.site.register(Profile)
admin.site.register(Time)