from django.urls import path

from .views_clips import (
    show_clips,
)
from .views_time import (
    show_times,
    add_new_face
)

urlpatterns = [
    path('show_clips', show_clips),
    path('show_times/<str:video_id>', show_times),
    path('analyze_clip/<str:video_id>', add_new_face),
]
