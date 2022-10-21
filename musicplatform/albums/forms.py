from django import forms

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    
class NewAlbumForm(forms.Form):
    name = forms.CharField(max_length=200)
    artist = forms.CharField(max_length=300)   
    release_date = forms.DateTimeField(widget=DateTimePickerInput, required=True)
    cost = forms.FloatField(required=True)