from django.urls import path
from . import views 

urlpatterns = [
    path('', views.playlist_list, name='playlist-list-page'),
    path('<int:id>', views.playlist_detail, name="playlist-detail-page"),
    path('update/<int:id>', views.playlist_update, name="playlist-update-page"),
    path('add-playlist', views.playlist_add, name="playlist-add-page"),
    path('yt-video/<int:id>', views.yt_video_detail, name='yt-video-detail-page'),
    path('yt-video/upadte/<int:id>', views.yt_video_update, name='yt-video-update-page'),
    path('yt-video-completed', views.yt_video_completed, name='yt-video-completed'),
    path('playlist-completed', views.playlist_completed, name='playlist-completed'),
    path('add-yt-video', views.yt_video_add, name='yt-video-add-page'),
]
