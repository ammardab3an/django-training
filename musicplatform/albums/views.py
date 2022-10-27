from django.views import View
from django.shortcuts import render
from albums.models import Album
from artists.models import Artist
from .forms import NewAlbumForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateAlbumView(LoginRequiredMixin, View):
    
    def get(self, request):
        return render(request, 'albums/new_album_form.html', {'form': NewAlbumForm()})
    
    def post(self, request):
        form = NewAlbumForm(request.POST)
        if form.is_valid():
            try:
                ar = Artist.objects.get(pk=form.cleaned_data['artist'])
                try:
                    Album.objects.create(
                        name=form.cleaned_data['name'],
                        artist=ar,
                        release_date=form.cleaned_data['release_date'],
                        cost=form.cleaned_data['cost'],
                    )
                    return render(request, 'albums/new_album_thanks.html', {'album_name': form.cleaned_data['name']})
                except Exception as e:
                    return render(request, 'albums/new_album_form.html', {'error_message': e, 'form': form})
            except Exception as e:
                return render(request, 'albums/new_album_form.html', {'error_message': e, 'form': form})
            