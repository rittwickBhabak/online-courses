from django.urls import path
from . import views 

urlpatterns = [
    path('', views.course_list, name='course-list-page'),
    path('<int:id>', views.course_detail, name='course-detail-page'),
    path('edit/<int:id>', views.course_edit, name='course-edit-page'),
    path('add', views.course_add, name='course-add-page'),
    path('video/<int:id>', views.video_detail, name='video-detail-page'),
    path('video/update/<int:id>', views.video_update, name='video-update-page'),
    path('storage', views.storage_list, name='storage-list-page'),
    path('storage/add', views.storage_add, name='storage-add-page'),
    path('chapter/update/<int:id>', views.chapter_update, name="chapter-update-page"),
    path('video-completed', views.video_completed, name="video-completed"),
    path('course-completed', views.course_completed, name="course-completed"),
]
