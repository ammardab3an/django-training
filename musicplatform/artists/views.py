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
            try:
                Artist.objects.create(name=form.cleaned_data['name'], social_media_link=form.cleaned_data['social_media_link'])
                return render(request, 'artists/new_artist_thanks.html', {'artist_name': form.cleaned_data['name']})
            except Exception as e:
                return render(request, 'artists/new_artist_form.html', {'error_message': e, 'form': form})

class ListAllArtistsView(View):
    
    def get(self, request):
        data = dict()
        for ar in Artist.objects.all().prefetch_related('album_set'):
            data[ar.name] = {
                'name': ar.name,
                'social_media_link': ar.social_media_link,
                'albums': ar.album_set.all(),
            }
        
        return render(request, 'artists/list_all.html', {'data': data})

