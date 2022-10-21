from msilib.schema import Error
from django.http import HttpResponseRedirect
from django.shortcuts import render
from artists.models import Artist
from .forms import NewArtistForm
from django.template.defaulttags import register

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

def get_artist(request):
    
    if request.method == 'POST':
        
        form = NewArtistForm(request.POST)
        
        if form.is_valid():
            try:
                Artist.objects.create(name=form.cleaned_data['name'], social_media_link=form.cleaned_data['social_media_link'])
                return render(request, 'artists/new_artist_thanks.html', {'artist_name': form.cleaned_data['name']})
            except Exception as e:
                return render(request, 'artists/new_artist_form.html', {'error_message': e, 'form': form})

    else:
        form = NewArtistForm()

    return render(request, 'artists/new_artist_form.html', {'form': form})

def get_artists(request):
    
    data = dict()
    for ar in Artist.objects.all().prefetch_related('album_set'):
        data[ar.name] = {
            'name': ar.name,
            'social_media_link': ar.social_media_link,
            'albums': ar.album_set.all(),
        }
    
    return render(request, 'artists/list_all.html', {'data': data})