from django.conf.urls import patterns, url

from ownWebsite import views

urlpatterns = patterns("", 
        url(r"^$", views.index, name="index"),
        url(r"^blog$", views.blog, name="blog"),
        url(r"^aboutme$", views.aboutme, name="aboutme"),
        url(r"^impressum$", views.impressum, name="impressum"),
        url(r"^projects$", views.projects, name="projects"),
        url(r"^travel$", views.travel, name="travel"),
        # url(r"^image", views.image, name="image"),
        # url(r"^sound", views.sound, name="sound"),
        # url(r"^change", views.change, name="change"),
        # url(r"^(?P<playlist_title>\w+)/$", views.playlistdetails, name="playlistdetails"),
)
