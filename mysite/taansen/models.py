from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

#class History(models.Model):     # History of each user
#    song_history = models.ManyToManyField(Song) #! on delete cascade is a syntax here
#    time = models.DateTimeField(auto_now_add=True)  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    history = models.OneToOneField(History, on_delete=models.CASCADE)
    liked_songs = models.ManyToManyField(Song, related_name='liked_songs')
    #history = models.OnetoOneField(History, related_name='song_history')
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

