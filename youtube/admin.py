from django.contrib import admin
from youtube.models import Playlist, YTVideo

# Register your models here.
admin.site.register(Playlist)
admin.site.register(YTVideo)