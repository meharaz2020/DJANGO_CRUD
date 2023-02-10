from django import forms
from first import models 


class MusicainForm(forms.ModelForm):
    class Meta:
        model=models.Musician
        fields="__all__"
class AlbumForm(forms.ModelForm):
    class Meta:
        model=models.Album
        fields="__all__"