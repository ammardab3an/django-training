import datetime
from albums.models import Album
from artists.models import Artist
from django.utils import timezone

def reset():
    
    Artist.objects.all().delete()
    Album.objects.all().delete()
        
    artists_obj = (
        Artist("artist0", "fb.com/artist0"),
        Artist("artist1", "fb.com/artist1"),
        Artist("artist2", "fb.com/artist2"),
        Artist("artist3", "fb.com/artist3"),
        Artist("artist4", "fb.com/artist4"),
        # Artist("artist5", "fb.com/artist5"),
        # Artist("artist6", "fb.com/artist6"),
        # Artist("artist7", "fb.com/artist7"),
        # Artist("artist8", "fb.com/artist8"),
        # Artist("artist9", "fb.com/artist9"),
    )

    albums_obj = (
        
        Album(0, "album0", "artist0", timezone.now()-datetime.timedelta(days=0), timezone.now()+datetime.timedelta(days=0), 10.0),
        Album(1, "album1", "artist0", timezone.now()-datetime.timedelta(days=1), timezone.now()+datetime.timedelta(days=7), 10.1),
        Album(2, "album2", "artist0", timezone.now()-datetime.timedelta(days=2), timezone.now()+datetime.timedelta(days=14), 10.2),
        
        Album(3, "album3", "artist1", timezone.now()-datetime.timedelta(days=0), timezone.now()+datetime.timedelta(days=10), 10.3),
        Album(4, "album4", "artist1", timezone.now()-datetime.timedelta(days=10), timezone.now()-datetime.timedelta(days=2), 10.4),
        
        Album(5, "album5", "artist2", timezone.now()-datetime.timedelta(days=30), timezone.now()-datetime.timedelta(days=10), 10.5),
        Album(6, "album6", "artist2", timezone.now()-datetime.timedelta(days=0), timezone.now()+datetime.timedelta(days=1), 10.6),
        
        Album(7, "album7", "artist3", timezone.now()-datetime.timedelta(days=1), timezone.now()+datetime.timedelta(days=1), 10.7),
    )

    Artist.objects.bulk_create(artists_obj)
    Album.objects.bulk_create(albums_obj)
