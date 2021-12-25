from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .setializers import *

# class ArtistApiViewSet(ModelViewSet):
#     serializer_class = ArtistSerializer
#     queryset = Artist.objects.all()
#
#     @action(methods=["GET"], detail=True, url_path='albums')
#     def get_albums(self, request, *args, **kwargs):
#         artist = self.get_object()
#         albums = Album.objects.filter(artist=artist)
#         ser = AlbumSerializer(albums,many=True)
#         return Response(ser.data)
#
#     @action(methods=["POST"], detail=True, url_path='album')
#     def post_songs(self, request, *args, **kwargs):
#         artist = self.get_object()
#         album= request.data
#         album["artist"] = artist.id
#         ser = SongSerializer(data=album)
#         if ser.is_valid():
#             ser.save()
#         return Response(ser.data)
# class AlbumApiViewSet(ModelViewSet):
#     serializer_class = AlbumSerializer
#     queryset = Album.objects.all()
#
#     @action(methods=["GET"],detail=True,url_path='songs')
#     def get_songs(self,request,*args,**kwargs):
#         album = self.get_object()
#         songs = Song.objects.filter(album=album)
#         ser = SongSerializer(songs,many=True)
#         return Response(ser.data)
#
#     @action(methods=["POST"], detail=True, url_path='song')
#     def post_songs(self, request, *args, **kwargs):
#         album = self.get_object()
#         song = request.data
#         song["album"] = album.id
#         ser = SongSerializer(data=song)
#         if ser.is_valid():
#             ser.save()
#         return Response(ser.data)
# class SongApiViewSet(ModelViewSet):
#     serializer_class = SongSerializer
#     queryset = Song.objects.all()
#     pagination_class = LimitOffsetPagination

class ArtistListApiView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["name"]
    search_fields = ["name", "description"]

class ArtistCreateApiView(CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistUpdateApiView(UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDestroyApiView(DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRetrieveApiView(RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumCreateApiView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumListApiView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumUpdateApiView(UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDestroyApiView(DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumRetrieveApiView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongCreateApiView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongListApiView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongUpdateApiView(UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDestroyApiView(DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongRetrieveApiView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

