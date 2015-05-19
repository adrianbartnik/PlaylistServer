from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone

from Playlist.models import *
from Playlist.forms import UserProfileForm, UserForm
from Playlist.serializers import PlaylistSerializer, UserSerializer
# from snippets.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

def overview(request):
    name = request.POST.get("name")

    if name in ['settings', 'user', 'register', 'login', 'logout']:
        return HttpResponseRedirect(reverse('Playlist:overview'))

    if name:
        playlist = Playlist.objects.get_or_create(name=name)[0]
        playlist.save()
        playlist.userprofile_set.add(request.user.userprofile)
    allplaylists = Playlist.objects.all()

    return render(request, "Playlist/overview.html", {"playlists": allplaylists, "popupmessages": []})

def playlist_view(request, playlist_name=""):
    u = request.POST.get("url")
    t = request.POST.get("title")
    p = request.POST.get("plattform")

    if t and u and p:
        track = Track(title=t,
                plattform=p,
                url=u,
                pub_date=timezone.now(), 
                playlist=Playlist.objects.get(name=playlist_name))
        track.save()

    delt = request.POST.get("deltitle")
    if delt: 
        Track.objects.get(id=delt).delete()

    p = get_object_or_404(Playlist, name=playlist_name)
    editable = False
    if request.user.is_authenticated():
        if request.user.userprofile in Playlist.objects.get(name=playlist_name).userprofile_set.all():
            editable = True
    
    return render(request, "Playlist/playlistdetails.html", {"playlist":p, 'CanEdit': editable})

def user_view(request, user_name=""):

    if not user_name:
        return render(request, "Playlist/user_overview.html", {'users': User.objects.all()[:5]})

    try:
        user = User.objects.get(username=user_name)

        return render(request, "Playlist/user.html", {})

    except ObjectDoesNotExist:
        user = None
        
    return render(request, "Playlist/user.html", {})

def settings_view(request):

    if request.user.is_authenticated():

        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

        return render(request, "Playlist/settings.html", {'user_form': user_form, 'profile_form': profile_form})

    else:
        return render(request, "Playlist/settings.html", {})

def register_view(request):
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

            user = authenticate(username=user.username, password=request.POST.get('password'))

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('Playlist:overview'))

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Playlist:overview'))
            else:
                return HttpResponse('Account not active yet')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'Playlist/login.html', {'error': True})

    else:
        return render(request, 'Playlist/login.html', {})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

# @api_view(('GET', ))
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)})
