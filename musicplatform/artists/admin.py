from django.contrib import admin
from .models import Artist
from django import forms
from albums.admin import AlbumInline

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'approvedAlbums']

    def approvedAlbums(self, obj):
        result = obj.album_set.filter(is_approved=True).count()
        return result

    approvedAlbums.short_description = "Approved Albums"
    approvedAlbums.admin_order_field = 'approved_albums'

    model = Artist
    
    inlines = [
        AlbumInline,
    ]