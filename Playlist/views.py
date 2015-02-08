from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from Playlist.models import *
from Playlist.forms import UserProfileForm, UserForm

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
        np.userprofile_set.add(request.user.userprofile)
    a = Playlist.objects.all()

    return render(request, "Playlist/overview.html", {"playlists":a })

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
    editable = False
    if request.user.is_authenticated():
        if request.user.userprofile in Playlist.objects.get(title=playlist_title).userprofile_set.all():
            editable = True
    
    return render(request, "Playlist/playlistdetails.html", {"playlist":p, 'CanEdit': editable})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'Playlist/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Playlist:overview'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Playlist:overview'))
            else:
                return HttpResponse('LOLZ! Account not active')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'Playlist/login.html', {'error': True})

    else:
        return render(request, 'Playlist/login.html', {})
