from django.core.checks import messages
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Playlist, YTVideo
import json
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def playlist_list(request):
    context = {
        'playlists': Playlist.objects.all()
    }
    return render(request, 'youtube/playlist_list.html', context=context)

def playlist_detail(request, id):
    context = {
        'playlist': get_object_or_404(Playlist, pk=id)
    }
    return render(request, 'youtube/playlist_detail.html', context=context)

def playlist_update(request, id):
    context = {

    }
    return render(request, 'youtube/.html', context=context)

def playlist_add(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            github_link = request.POST.get('github-link')
            youtube_link = request.POST.get('youtube-link')
            height = request.POST.get('height')
            width = request.POST.get('width')
            google_docs_link = request.POST.get('google-docs-link')
            youtube_videos = request.POST.get('youtube-videos')
            playlist = Playlist.objects.get_or_create(title=title, github_link=github_link, youtube_link=youtube_link, google_docs_link=google_docs_link, height=height, width=width)[0]
            data = json.loads(youtube_videos)
            videos = []
            try:
                for key, value in data.items():
                    yt_video_title = key
                    video_id = value['vid']
                    yt_video = YTVideo.objects.create(title=yt_video_title, video_id=video_id, playlist=playlist)
                    videos.append(yt_video)
                messages.success(request, 'New course created successfully.')
                redirect_path = reverse('playlist-detail-page', args=[playlist.id])
                return redirect(redirect_path)
            except:
                playlist.delete()
                messages.error(request, 'Some error occoured during adding videos. Failed to create new course.')
                redirect_path = reverse('playlist-add-page')
                return redirect(redirect_path)
        except:
            messages.error(request, 'Some error occoured. Failed to create new course.')
            redirect_path = reverse('playlist-add-page')
            return redirect(redirect_path)

    return render(request, 'youtube/playlist_add.html')

def yt_video_detail(request, id):
    video = get_object_or_404(YTVideo, pk=id)
    next_video = YTVideo.objects.filter(pk__gt=video.id, playlist=video.playlist).order_by('id').first()
    prev_video = YTVideo.objects.filter(pk__lt=video.id, playlist=video.playlist).order_by('-id').first()
    context = {
        'video': video,
        'next': next_video,
        'prev': prev_video
    }
    return render(request, 'youtube/yt_video_detail.html', context=context)

def yt_video_update(request, id):
    context = {

    }
    return render(request, 'youtube/.html', context=context)

def yt_video_completed(request):
    if request.method == 'POST':
        vid = request.POST.get('vid')
        video = get_object_or_404(YTVideo, pk=vid)
        video.is_done = not video.is_done
        video.save()
        redirect_path = reverse('yt-video-detail-page', args=[video.id])
        return redirect(redirect_path)


def playlist_completed(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        playlist = get_object_or_404(Playlist, pk=pid)
        playlist.is_done = not playlist.is_done
        playlist.save()
        redirect_path = reverse('playlist-detail-page', args=[playlist.id])
        return redirect(redirect_path)

def yt_video_add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        vid = request.POST.get('vid')
        pid = request.POST.get('pid')
        playlist = get_object_or_404(Playlist, pk=pid)
        video = YTVideo.objects.create(title=title, video_id=vid, playlist=playlist)
        messages.success(request, 'New Video Added Successfully')
        redirect_path = reverse('playlist-detail-page', args=[pid])
        return redirect(redirect_path)