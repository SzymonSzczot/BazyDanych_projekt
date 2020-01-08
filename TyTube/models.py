from django.db import models

# Create your models here.

class Clips(models.Model):
    link = models.CharField(max_length=128, unique=True)
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, unique=False)
    duration = models.PositiveIntegerField(unique=False)
    face_recognized_count = models.PositiveIntegerField(null=True)
    face_on_screen_time = models.PositiveIntegerField(null=True)
    views = models.CharField(max_length=100, unique=False)
    votes = models.CharField(max_length=100, unique=False)
    thumbnail = models.CharField(max_length=128)
    upload_date = models.DateField(unique=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WhenFaceAppears(models.Model):
    video = models.ForeignKey(Clips, on_delete=models.CASCADE, verbose_name="video")
    appeared_start = models.PositiveIntegerField(unique=False)
    appeared_end = models.PositiveIntegerField(unique=False)
    link = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appeared_start']