from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __unicode__(self):
        # return unicode(self.title + " " + self.pub_date)
        return self.title
