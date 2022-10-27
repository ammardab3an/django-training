from logging import exception
from msilib.schema import Error
from django.http import HttpResponseRedirect
from django.shortcuts import render
from albums.models import Album
from artists.models import Artist

from .forms import NewAlbumForm

def get_album(request):
    
    if request.method == 'POST':
        
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

    else:
        form = NewAlbumForm()

    return render(request, 'albums/new_album_form.html', {'form': form})
