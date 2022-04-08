from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name


class MovieAlbum(models.Model):
    title = models.TextField()
    release_year = models.DateField()
    actor = models.ManyToManyField(Actor) # StarsIn relation, a many-many field
    artist = models.ManyToManyField(Artist) # SungIn relation, a many-many field

    def __str__(self):
        return self.title

class Song(models.Model):
    # an id primary key is already added by django, hence
    # not required to add explicitly anywhere - VSR
    # refer: https://docs.djangoproject.com/en/4.0/topics/db/models/#automatic-primary-key-fields
    title = models.TextField()
    genre = models.TextField()
    lyrics = models.TextField(default="NA") #! might need to handle the case when someone searches for say 'NA' in the lyrics
    # !tags = {}
    # !path_to_lyrics = 
    image = models.ImageField() #!
    audio_file = models.FileField() #!
    #audio_link =  models.CharField(max_length=200) #!
    duration=models.CharField(max_length=20) #!
    paginate_by = 2 #!
    movie_album = models.ForeignKey(MovieAlbum, on_delete=models.CASCADE) #SongOf relation. One song can belong to one album, while one album may host many songs.
    artist = models.ManyToManyField(Artist) # SungBy relation. A many-many field.

    def __str__(self):
        return self.title
  
class User(models.Model):
    password = models.TextField()
    username = models.TextField()
    user_type = models.BooleanField() # added it as a boolean field. Choose the convention or just remove it - VSR
    #! IMP: Liked songs and history(which will be a list of songs)
    #! is left for now. Looks doable though