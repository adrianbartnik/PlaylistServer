from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin

from RestFramework import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r"^polls/", include("polls.urls")),
    url(r"^playlist/", include("Playlist.urls", app_name="PlaylistApp", namespace="Playlist")),
    
    url(r"^website/", include("ownWebsite.urls", app_name="ownWebsite", namespace="ownWebsite")),

    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
) 

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('django.views.static', 
            (r'media/(?P<path>.*)', 
            'serve', 
            {'document_root': settings.MEDIA_ROOT}), )
