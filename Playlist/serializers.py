from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from Playlist.models import Playlist, UserProfile, Track

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.ReadOnlyField(source='userprofile_set.all()[0].username', read_only=True)
    # owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Playlist
        fields = ('pub_date', 'title', 'user', )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        # fields = ('id', 'username', 'snippets')
        fields = ('id', 'username', )
