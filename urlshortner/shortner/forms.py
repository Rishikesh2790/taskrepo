from .models import ShortUrl
from django import forms

class URLForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['long_url']
