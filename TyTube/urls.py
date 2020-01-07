from django.urls import path

from .views_clips import (
    show_clips,
)
from .views_time import (
    show_times,
)

urlpatterns = [
    path('show_clips', show_clips),
    path('show_times/<str:video_id>', show_times),
]
