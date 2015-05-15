from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers, viewsets
from Playlist import views

router = DefaultRouter()
router.register(r'playlist', views.PlaylistViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns("", 
    url(r"^$", views.overview, name="overview"),
    url(r"^register", views.register, name="register"),
    url(r"^login", views.user_login, name="login"),
    url(r"^logout", views.logout_view, name="logout"),
    url(r'^api/', include(router.urls)),
    url(r"^(?P<playlist_name>\w+)/$", views.playlistdetails, name="playlistdetails"),
)
