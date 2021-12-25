from .models import *
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=['id','name','photo','description']
class AlbumSerializer(serializers.ModelSerializer):
    # artist = ArtistSerializer()
    class Meta:
        model=Album
        fields=['id','name','cover','artist']
class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer()
    class Meta:
        model=Song
        fields=['id','name','cover','lyrics','duration','album','source']
