from django import forms
from django.contrib.auth.models import User
from Playlist.models import Track, Playlist, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text="")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    soundcloud = forms.CharField(required=False)
    youtube = forms.CharField(required=False)
    picture = forms.ImageField(help_text="", required=False)

    class Meta:
        model = UserProfile
        fields = ('picture', 'youtube', 'soundcloud', )
