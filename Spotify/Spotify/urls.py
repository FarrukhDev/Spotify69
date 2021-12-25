from django.contrib import admin
from django.urls import path, include
from music.views import ArtistListApiView,AlbumListApiView,SongListApiView,SongCreateApiView, SongUpdateApiView, SongDestroyApiView, AlbumCreateApiView, \
    AlbumUpdateApiView, AlbumDestroyApiView, ArtistCreateApiView, ArtistUpdateApiView, ArtistDestroyApiView,ArtistRetrieveApiView, AlbumRetrieveApiView, SongRetrieveApiView
# from rest_framework.routers import DefaultRouter
#
# router=DefaultRouter()
# router.register('artist',ArtistApiViewSet)
# router.register('album',AlbumApiViewSet)
# router.register('song',SongApiViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(router.urls)),
    path('artist/',ArtistListApiView.as_view(),name='artist-list'),
    path('album/',AlbumListApiView.as_view(),name='album-list'),
    path('song/',SongListApiView.as_view(),name='song-list'),
    path('songpost/',SongCreateApiView.as_view(),name='song-post'),
    path('songput/<int:pk>',SongUpdateApiView.as_view(),name='song-put'),
    path('songdel/<int:pk>',SongDestroyApiView.as_view(),name='song-delete'),
    path('album/',AlbumCreateApiView.as_view(),name='album-post'),
    path('albumput/<int:pk>',AlbumUpdateApiView.as_view(),name='album-put'),
    path('albumdel/<int:pk>',AlbumDestroyApiView.as_view(),name='album-delete'),
    path('artistpost/', ArtistCreateApiView.as_view(), name='artist-post'),
    path('artists/<int:pk>', ArtistUpdateApiView.as_view(), name='artist-put'),
    path('artistdel/<int:pk>', ArtistDestroyApiView.as_view(), name='artist-delete'),
    path('artistget/<int:pk>', ArtistRetrieveApiView.as_view(), name='artist-get'),
    path('albumget/<int:pk>', AlbumRetrieveApiView.as_view(), name='album-get'),
    path('songget/<int:pk>', SongRetrieveApiView.as_view(), name='song-get'),


]
