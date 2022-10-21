import datetime
from albums.models import Album
from artists.models import Artist
from django.utils import timezone
import inspect

def reset():
    
    Artist.objects.all().delete()
    Album.objects.all().delete()
        
    artists_obj = (
        Artist(name="artist0", social_media_link="fb.com/artist0"),
        Artist(name="artist1", social_media_link="fb.com/artist1"),
        Artist(name="artist2", social_media_link="fb.com/artist2"),
        Artist(name="artist3", social_media_link="fb.com/artist3"),
        Artist(name="artist4", social_media_link="fb.com/artist4"),
    )

    Artist.objects.bulk_create(artists_obj)
    
    albums_obj = (
        Album(name="album0", artist=Artist.objects.get(pk="artist0"), release_date=timezone.now()+datetime.timedelta(days=0), cost=10.0),
        Album(name="album1", artist=Artist.objects.get(pk="artist0"), release_date=timezone.now()+datetime.timedelta(days=7), cost=10.1),
        Album(name="album2", artist=Artist.objects.get(pk="artist0"), release_date=timezone.now()+datetime.timedelta(days=14), cost=10.2),
        Album(name="album3", artist=Artist.objects.get(pk="artist1"), release_date=timezone.now()+datetime.timedelta(days=10), cost=10.3),
        Album(name="album4", artist=Artist.objects.get(pk="artist1"), release_date=timezone.now()-datetime.timedelta(days=2), cost=10.4),
        Album(name="album5", artist=Artist.objects.get(pk="artist2"), release_date=timezone.now()-datetime.timedelta(days=10), cost=10.5),
        Album(name="album6", artist=Artist.objects.get(pk="artist2"), release_date=timezone.now()+datetime.timedelta(days=1), cost=10.6),
        Album(name="album7", artist=Artist.objects.get(pk="artist3"), release_date=timezone.now()+datetime.timedelta(days=1), cost=10.7),
    )

    Album.objects.bulk_create(albums_obj)

def print_md(cnt, desc, fn, no_output=False):
    
    print('##### ', cnt, '. ', desc, sep='')
    
    print('\ncode:\n')
    print('```python')
    print(inspect.getsource(fn))
    print('```')
    
    if(not no_output):
        print('\noutput:\n')
        print('```')
    fn()
    if(not no_output):
        print('```')
        
    print()

def create_new_artists():
    new_artists = (
        Artist(name="ammar", social_media_link="fb.com/ammardab3an"),
        Artist(name="mahmoud", social_media_link="fb.com/mahmoud"),
        Artist(name="majed", social_media_link="fb.com/madjed"),
    )

    for ar in new_artists:
        ar.save()

def list_all_artists():
    for ar in Artist.objects.all():
        print(ar)
        
def list_artists_start_a():
    for ar in Artist.objects.filter(name__startswith='a'):
        print(ar)
        
def create_albums_two_ways():
    #first way
    ar_ammar = Artist.objects.get(pk="ammar")
    al0 = Album(name="ammars_first_album", artist=ar_ammar, 
                release_date=timezone.now()+datetime.timedelta(weeks=1), 
                cost=20.50)
    al0.save()
    
    #second way
    ar_ammar.album_set.create(name="ammars_second_album", 
                                release_date=timezone.now()+datetime.timedelta(days=1), 
                                cost=30.30)
    
    for al in ar_ammar.album_set.all():
        print(al)

def latest_release_album():
    al = Album.objects.latest('release_date')
    print(al, al.release_date)

def list_albums_lt_today():
    albums_released_lt_today = Album.objects.filter(release_date__lt=timezone.now()).order_by('-release_date')
    for al in albums_released_lt_today:
        print(al, al.release_date.date())
    
def list_albums_lte_today():
    albums_released_lte_today = Album.objects.filter(release_date__lte=timezone.now()-datetime.timedelta(days=1)).order_by('-release_date')
    for al in albums_released_lte_today:
        print(al, al.release_date.date())

def albums_count():
    tot_albums = Album.objects.count()
    print(tot_albums)

def list_artists_with_albums_st_way():
    for ar in Artist.objects.all():
        print(ar)
        ar_albums = ar.album_set.all()
        for al in ar_albums:
            print('\t', al.name, al.release_date.date(), al.cost)
        if not ar_albums:
            print('\t', 'no albums yet.')
        

def list_artists_with_albums_nd_way():
    for ar in Artist.objects.all():
        print(ar)
        ar_albums = Album.objects.filter(artist=ar)
        for al in ar_albums:
            print('\t', al.name, al.release_date.date(), al.cost)
        if not ar_albums:
            print('\t', 'no albums yet.')

def list_albums_by_cost_name():
    albums_ordered_by_cost_name = Album.objects.order_by('cost', 'name')
    for al in albums_ordered_by_cost_name:
        print(al, ', cost: ', al.cost, sep='')

def main():
    reset()
    print_md(1, 'create new artists.', create_new_artists, True)
    print_md(2, 'all artists sorted by name.', list_all_artists)
    print_md(3, "all artists whose names starts with 'a'.", list_artists_start_a)
    print_md(4, "create albums using two different ways.", create_albums_two_ways)
    print_md(5, 'latest release date album.', latest_release_album)
    print_md(6, 'albums released before today.', list_albums_lt_today)
    print_md(6, 'albums released today or before today.', list_albums_lte_today)
    print_md(7, 'albums total count.', albums_count)
    print_md(8, 'list all artists with their albums (1st way).', list_artists_with_albums_st_way)
    print_md(9, 'list all artists with their albums (2nd way).', list_artists_with_albums_nd_way)
    print_md(10, 'list all albums ordered by cost then name.', list_albums_by_cost_name)