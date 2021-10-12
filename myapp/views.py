from django.db.models.fields import CharField
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Storage, Course, Chapter, Video
from django.contrib import messages 
from django.urls import reverse

import json 
from datetime import datetime 

# Create your views here.
def create_chapters_and_videos(course, json_string):
    data = json.loads(json_string) 
    try:
        for chapter, value in data.items():
            print(chapter)
            videos = value['videos']
            chapter = Chapter.objects.create(title=chapter, course=course)
            for video, link_value in videos.items():
                link = link_value['link']
                if video.endswith('.mp4'):
                    Video.objects.create(chapter=chapter, title=video[:-4], download_page=link, type='video')
                else:
                    Video.objects.create(chapter=chapter, title=video, download_page=link, type='unknown')

    except Exception as e:
        print(e)
    
def update_chapters_and_videos(course, json_string):
    pass 

def course_list(request):
    context = {
        'courses': Course.objects.all()
    } 
    return render(request, 'myapp/course_list.html', context=context)

def course_detail(request, id):
    course = get_object_or_404(Course, pk=id)
    chapters = course.chapter_set.all()
    videos = Video.objects.all()
    last_seen = None 
    videos = list(filter(lambda x: x.chapter in chapters, videos))
    videos = sorted(videos, key=lambda x: x.last_seen)
    last_seen = videos[-1]


    context = {
        'course': course,
        'last_seen': last_seen
    }
    return render(request, 'myapp/course_detail.html', context=context)

def course_edit(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        google_docs_link = request.POST.get('google_docs_link')
        link = request.POST.get('link')
        chapters_videos_json = request.POST.get('chapters-videos-json')
        course = get_object_or_404(Course, pk=id)
        try:
            course.title = title
            course.google_docs_link = google_docs_link
            course.link = link
            course.chapters_videos_json = chapters_videos_json
            course.save()
            messages.success(request, 'The course is updated successfully.')
            redirect_path = reverse('course-detail-page', args=[id])
            HttpResponseRedirect(redirect_path)
        except:
            messages.error(request, 'Failed to edit the course. Some error occoured.')
            redirect_path = reverse('course-edit-page', args=[id])
            HttpResponseRedirect(redirect_path)
    else:
        context = {
            'course': get_object_or_404(Course, pk=id)
        }
        return render(request, 'myapp/course_update.html', context=context)

def course_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        google_docs_link = request.POST.get('google_docs_link')
        link = request.POST.get('link')
        chapters_videos_json = request.POST.get('chapters-videos-json')
        try:
            course = Course.objects.create(title=title, google_docs_link=google_docs_link, link=link, chapters_videos_json=chapters_videos_json)
            create_chapters_and_videos(course, chapters_videos_json)
            messages.success(request, 'Course created successfully.')
            redirect_path = reverse('course-detail-page', args=[course.pk])
        except:
            messages.error(request, 'Failed to create new course. Some error occoured.')
            redirect_path = reverse('course-add-page')
        return redirect(redirect_path)
    else:
        context = {
            'storages': Storage.objects.all()
        }
        return render(request, 'myapp/course_add.html', context=context)

def video_detail(request, id):
    video = get_object_or_404(Video, pk=id)
    video.last_seen = datetime.now()
    video.save()
    next_video = Video.objects.filter(chapter=video.chapter, id__gt=video.id).order_by('id').first()
    prev_video = Video.objects.filter(chapter=video.chapter, id__lt=video.id).order_by('-id').first()
    context = {
        'video': video,
        'next': next_video,
        'prev': prev_video
    }
    return render(request, 'myapp/video_detail.html', context=context)

def video_update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        download_page = request.POST.get('download-page')
        download_link = request.POST.get('download-link')
        video = get_object_or_404(Video, pk=int(id))
        try:
            video.title = title
            video.download_page = download_page
            video.download_link = download_link
            video.save()
            messages.success(request, 'The video is updated successfully.')
            redirect_path = reverse('video-detail-page', args=[id])
        except:
            messages.error(request, 'Failed to update the video. Some error occoured.')
            redirect_path = reverse('video-update-page', args=[id])
        return HttpResponseRedirect(redirect_path)
    else:
        context = {
            'video': get_object_or_404(Video, pk=id)
        }
        return render(request, 'myapp/video_update.html', context=context)

def storage_list(request):
    context = {
        'storages': Storage.objects.all()
    }
    return render(request, 'myapp/storage_list.html', context=context)

def storage_add(request):
    redirect_path = reverse('storage-list-page')
    if request.method == "POST":
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            description = request.POST.get('description')
            Storage.objects.create(email = email, password = password, description = description)
            messages.success(request, 'New storage added.') 
        except:
            messages.error(request, 'Failed to add new storage.') 
    return HttpResponseRedirect(redirect_path)

def chapter_update(request, id):
    if request.method == 'POST':
        chapter = get_object_or_404(Chapter, pk=id)
        title = request.POST.get('title')
        google_docs_link = request.POST.get('google-docs-link')
        chapter.title = title
        chapter.google_docs_link = google_docs_link
        chapter.save()
        messages.success(request, 'Chapter updated successfully.')
        return redirect(reverse('chapter-update-page', args=[id]))
    else:
        context = {
            'chapter': get_object_or_404(Chapter, pk=id)
        }
        return render(request, 'myapp/chapter_update.html', context=context)
