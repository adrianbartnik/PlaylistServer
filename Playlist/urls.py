from django.conf.urls import patterns, url

from Playlist import views

urlpatterns = patterns("", 
        url(r"^$", views.overview, name="overview"),
        url(r"^image", views.image, name="image"),
        url(r"^sound", views.sound, name="sound"),
        url(r"^change", views.change, name="change"),
        url(r"^register", views.register, name="register"),
        url(r"^login", views.user_login, name="login"),
        url(r"^logout", views.logout_view, name="logout"),
        url(r"^(?P<playlist_title>\w+)/$", views.playlistdetails, name="playlistdetails"),
)
