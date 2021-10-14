from django.db import models

# Create your models here.
class Playlist(models.Model):
    title = models.CharField(max_length=1000)
    github_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField()
    is_done = models.BooleanField(default=False)
    google_docs_link = models.URLField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.title 

class YTVideo(models.Model):
    title = models.CharField(max_length=1000)
    video_id = models.CharField(max_length=30)
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    seen_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.playlist.title}"