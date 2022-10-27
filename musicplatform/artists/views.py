from django.views import View
from django.shortcuts import render
from artists.models import Artist
from .forms import NewArtistForm
from django.template.defaulttags import register
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateArtistView(LoginRequiredMixin, View):
    
    def get(self, request):
        return render(request, 'artists/new_artist_form.html', {'form': NewArtistForm()})
    
    def post(self, request):
        form = NewArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'artists/new_artist_thanks.html', {'artist_name': form.cleaned_data['name']})
        else:
            return render(request, 'artists/new_artist_form.html', {'error_message': 'invalid request', 'form': form})

class ListAllArtistsView(View):
    
    def get(self, request):
        data = Artist.objects.all().prefetch_related('album_set', 'album_set__song_set')
        return render(request, 'artists/list_all.html', {'data': data})

