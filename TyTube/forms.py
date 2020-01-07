from django import forms

from .models import (
    Clips,
    WhenFaceAppears,
)


class ClipsModelForm(forms.ModelForm):
    class Meta:
        model = Clips
        fields = ['link']


class WhenFaceAppearsModelForm(forms.ModelForm):
    class Meta:
        model = WhenFaceAppears
        fields = ['video', 'appeared_start', 'appeared_end']
