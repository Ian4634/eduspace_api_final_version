from django import forms
from .models import Video

class AddVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = (
            'name',
            'source',
            'descriptions'
        )
