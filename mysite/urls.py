from django.contrib import admin
from django.urls import include, path
from .views import main
from TyTube.views import (
    create_clip,
    create_time,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', main),
    path('main/', main),
    path('create_clip/', create_clip),
    path('create_time/', create_time),
    path('main/', include('TyTube.urls'))
]
