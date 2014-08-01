from django.db import models

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
