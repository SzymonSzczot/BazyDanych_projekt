from django.db import models

# Create your models here.


class Clips(models.Model):
    name = models.CharField(max_length=100, unique=False)
    duration = models.PositiveIntegerField(unique=False)
    canal = models.CharField(max_length=100, unique=False)
    positive_voices = models.PositiveIntegerField(unique=False)
    negative_voices = models.PositiveIntegerField(unique=False)
    uploaded_date = models.DateField(unique=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WhenFaceAppears(models.Model):
    video = models.ForeignKey(Clips, on_delete=models.CASCADE, verbose_name="video")
    appeared_start = models.TimeField(unique=False)
    appeared_end = models.TimeField(unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
