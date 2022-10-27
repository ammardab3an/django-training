from django.views import View
from django.shortcuts import render
from albums.models import Album, Song
from artists.models import Artist
from .forms import NewAlbumForm, NewSongForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateAlbumView(LoginRequiredMixin, View):
    
    def get(self, request):
        return render(request, 'albums/new_album_form.html', {'form': NewAlbumForm()})
    
    def post(self, request):
        form = NewAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'albums/new_album_thanks.html', {'album_name': form.cleaned_data['name']})
        else:
            return render(request, 'albums/new_album_form.html', {'error_message': 'invalid request', 'form': form})

class CreateSongView(LoginRequiredMixin, View):
    
    def get(self, request):
        return render(request, 'albums/new_song_form.html', {'form': NewSongForm()})
    
    def post(self, request):
        form = NewSongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'albums/new_song_thanks.html', {'song_name': form.cleaned_data['name']})
        else:
            return render(request, 'albums/new_song_form.html', {'error_message': 'invalid request', 'form': form})
    
    