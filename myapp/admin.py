from django.contrib import admin
from .models import Course, Video, Storage, Chapter
admin.site.site_header = 'Online Courses Admin'
admin.site.site_title = 'Online Courses Admin Area'
admin.site.index_title = 'Welcome to the Online Courses admin area'
# Register your models here.
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Storage)
admin.site.register(Chapter)