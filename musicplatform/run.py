import datetime
from albums.models import Album
from artists.models import Artist
from django.utils import timezone
from reset_db import reset

reset()

new_artists = (
    Artist("ammar", "fb.com/ammardab3an"),
    Artist("mahmoud", "fb.com/mahmoud"),
    Artist("majed", "fb.com/madjed"),
)

for ar in new_artists:
    ar.save()
    
print("all artists sorted by name:")
for ar in Artist.objects.all():
    print(ar)

print()

print("all artists whose names starts with 'a':")
for ar in Artist.objects.filter(name__startswith='a'):
    print(ar)

print()

ar_ammar = Artist.objects.get(pk="ammar")
al0 = Album(name="ammars_first_album", artist=ar_ammar, creation_date=timezone.now()-datetime.timedelta(days=1), release_date=timezone.now()+datetime.timedelta(weeks=1), cost=20.50)
al0.save()

Album.objects.create(name="ammars_second_album", artist=ar_ammar, creation_date=timezone.now(), release_date=timezone.now()+datetime.timedelta(days=1), cost=30.30)

print("ammar's albums:")
for al in Artist.objects.get(pk="ammar").album_set.all():
    print(al)

print()

latest_release_album = Album.objects.order_by('-release_date')[:1].get()
print('latest album:')
print(latest_release_album, latest_release_album.release_date)

print()

albums_released_lt_today = Album.objects.filter(release_date__lt=timezone.now()).order_by('-release_date')
print('albums released before today:')
for al in albums_released_lt_today:
    print(al, al.release_date.date())
    
print()

albums_released_lte_today = Album.objects.filter(release_date__lte=timezone.now()-datetime.timedelta(days=1)).order_by('-release_date')
print('albums released today or before today:')
for al in albums_released_lte_today:
    print(al, al.release_date.date())

print()

tot_albums = Album.objects.count()
print('total number of albums:', tot_albums)

print()

print('first way:')
for ar in Artist.objects.all():
    print(ar)
    ar_albums = ar.album_set.all()
    for al in ar_albums:
        print('\t', al.name, al.release_date.date(), al.cost)
    if not ar_albums:
        print('\t', 'no albums yet.')
        
print()

print('second way:')
for ar in Artist.objects.all():
    print(ar)
    ar_albums = Album.objects.filter(artist=ar)
    for al in ar_albums:
        print('\t', al.name, al.release_date.date(), al.cost)
    if not ar_albums:
        print('\t', 'no albums yet.')

print()

print('all albums ordered my cost then name:')
albums_ordered_by_cost_name = Album.objects.order_by('cost', 'name')
for al in albums_ordered_by_cost_name:
    print(al, ', cost: ', al.cost, sep='')
    
print()
print ('end')