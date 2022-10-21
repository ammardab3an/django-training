from django import forms

class NewArtistForm(forms.Form):
    name = forms.CharField(max_length=300)
    social_media_link = forms.URLField(max_length=300, required=False)