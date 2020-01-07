from django.contrib import admin
from django.urls import include, path

from TyTube.views_clips import (
    create_clip,
)
from .views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', main),
    path('', main),
    path('main/', main),
    path('create_clip/', create_clip),

    path('main/', include('TyTube.urls'))
]
