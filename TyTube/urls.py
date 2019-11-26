from django.urls import path
from .views import (
    show_clips,
    show_times,
)

urlpatterns = [
    path('show_clips', show_clips),
    path('show_times', show_times),
]
