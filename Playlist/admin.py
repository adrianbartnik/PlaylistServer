from django.contrib import admin

from Playlist.models import UserProfile, Playlist, Track

admin.site.register(UserProfile)
admin.site.register(Playlist)
admin.site.register(Track)
