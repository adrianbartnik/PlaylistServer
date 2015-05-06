from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets

from RestFramework import views

admin.autodiscover()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r"^polls/", include("polls.urls")),
    url(r"^playlist/", include("Playlist.urls", app_name="PlaylistApp", namespace="Playlist")),
    
    url(r"^website/", include("ownWebsite.urls", app_name="ownWebsite", namespace="ownWebsite")),
    
    url('^snippets/', include('snippets.urls')),

    url('^', include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
)
