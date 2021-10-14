from datetime import datetime
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class Storage(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.email} {self.password}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    google_docs_link = models.URLField(null=True, blank=True)
    link = models.URLField()
    chapters_videos_json = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    google_docs_link = models.URLField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True, blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Video(models.Model):
    title = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    download_page = models.URLField()
    download_link = models.URLField(null=True, blank=True)
    last_seen = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    is_visited = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} from {self.chapter.title} of course {self.chapter.course.title}"
