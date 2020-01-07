from django import forms

from .models import (
    Clips
)


class ClipsModelForm(forms.ModelForm):
    class Meta:
        model = Clips
        fields = ['link']






