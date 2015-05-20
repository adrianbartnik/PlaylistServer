from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers, viewsets
from Playlist import views

router = DefaultRouter()
router.register(r'playlist', views.PlaylistViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns("", 
    url(r"^$", views.overview, name="overview"),
    url(r"^register", views.register_view, name="register"),
    url(r"^login", views.login_view, name="login"),
    url(r"^logout", views.logout_view, name="logout"),
    url(r"^settings", views.settings_view, name="settings"),
    url(r"^(?P<user_name>\w+)/$", views.user_view, name="user"),
    url(r"^(?P<user_name>\w+)/(?P<playlist_name>\w+)/$", views.playlist_view, name="playlistdetails"),
    url(r'^api/', include(router.urls)),
)
