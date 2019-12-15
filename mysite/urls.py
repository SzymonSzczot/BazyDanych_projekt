from django.contrib import admin
from django.urls import include, path

from TyTube.views_clips import (
    create_clip,
)
from TyTube.views_time import (
    create_time,
)
from .views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', main),
    path('', main),
    path('main/', main),
    path('create_clip/', create_clip),
    path('create_time/', create_time),
    path('main/', include('TyTube.urls'))
]
