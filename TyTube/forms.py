from django import forms

from .models import (
    Clips,
    WhenFaceAppears,
)


class ClipsModelForm(forms.ModelForm):
    class Meta:
        model = Clips
        fields = ['link', 'title', 'duration', 'canal', 'positive_voices', 'negative_voices']


class WhenFaceAppearsModelForm(forms.ModelForm):
    class Meta:
        model = WhenFaceAppears
        fields = ['video', 'appeared_start', 'appeared_end']
