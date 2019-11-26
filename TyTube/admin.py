from django.contrib import admin

# Register your models here.
from .models import (
    Clips,
    WhenFaceAppears
)

admin.site.register(Clips)
admin.site.register(WhenFaceAppears)
