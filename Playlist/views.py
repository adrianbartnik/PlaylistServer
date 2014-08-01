from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from Playlist.models import *

def image(request):
    return render_to_response("Playlist/image.html")

def sound(request):
    return render_to_response("Playlist/sound.html")

def change(request):
    return render_to_response("Playlist/change.html")

def overview(request):
    p = request.POST.get("name")
    if p:
        np = Playlist(pub_date=timezone.now(), title=p)
        np.save()
    a = Playlist.objects.all()
    return render(request, "Playlist/overview.html", {"playlists":a})

def playlistdetails(request, playlist_title=""):
    u = request.POST.get("url")
    t = request.POST.get("title")
    p = request.POST.get("plattform")
    if t and u and p:
        track = Track(title=t,
                plattform=p,
                url=u,
                pub_date=timezone.now(), 
                playlist=Playlist.objects.get(title=playlist_title))
        track.save()

    delt = request.POST.get("deltitle")
    if delt: 
        Track.objects.get(id=delt).delete()

    p = get_object_or_404(Playlist, title=playlist_title)
    return render(request, "Playlist/playlistdetails.html", {"playlist":p})
