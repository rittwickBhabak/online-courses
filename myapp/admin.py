from django.contrib import admin
from .models import Course, Video, Storage, Chapter

# Register your models here.
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Storage)
admin.site.register(Chapter)