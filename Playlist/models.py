from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __unicode__(self):
        return self.title 


class Track(models.Model):
    playlist = models.ForeignKey(Playlist)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    plattform = models.IntegerField()
    # 0 Youtube
    # 1 Soundcloud
    pub_date = models.DateTimeField("date published")

    def __unicode__(self):
        return self.title 

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    playlists = models.ManyToManyField(Playlist)

    def __unicode__(self):
        return self.user.username
