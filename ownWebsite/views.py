from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from ownWebsite.models import *

def index(request):
    return render_to_response("ownWebsite/Index.html")

def aboutme(request):
    return render_to_response("ownWebsite/AboutMe.html")

def impressum(request):
    return render_to_response("ownWebsite/Impressum.html")

def projects(request):
    return render_to_response("ownWebsite/Projects.html")

def travel(request):
    return render_to_response("ownWebsite/Travel.html")

def blog(request):
    if request.GET.get("all"): 
        p = Post.objects.all().order_by('pub_date')
        print "LOLZ"
    else:
        p = Post.objects.all().order_by('pub_date').reverse()[0:3]
    return render(request, "ownWebsite/Blog.html", {"posts": p, "all": request.GET.get("all")})

# def overview(request):
#     p = request.POST.get("name")
#     if p:
#         np = Playlist(pub_date=timezone.now(), title=p)
#         np.save()
#     a = Playlist.objects.all()
#     return render(request, "Playlist/overview.html", {"playlists":a})

# def playlistdetails(request, playlist_title=""):
#     u = request.POST.get("url")
#     t = request.POST.get("title")
#     p = request.POST.get("plattform")
#     if t and u and p:
#         track = Track(title=t,
#                 plattform=p,
#                 url=u,
#                 pub_date=timezone.now(), 
#                 playlist=Playlist.objects.get(title=playlist_title))
#         track.save()

#     delt = request.POST.get("deltitle")
#     if delt: 
#         Track.objects.get(id=delt).delete()

#     p = get_object_or_404(Playlist, title=playlist_title)
#     return render(request, "Playlist/playlistdetails.html", {"playlist":p})
