from socket import fromshare
from django.contrib import admin
from .models import Album
from django import forms
class AlbumForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['is_approved'].help_text = 'Approve the album if its name is not explicit'

    class Meta:
        model = Album
        exclude = ()
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist']
    readonly_fields = ['creation_date']
    form = AlbumForm

class AlbumInline(admin.TabularInline):
    model = Album
    