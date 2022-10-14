##### 1. create new artists.

code:

```python
def create_new_artists():
    new_artists = (
        Artist("ammar", "fb.com/ammardab3an"),
        Artist("mahmoud", "fb.com/mahmoud"),
        Artist("majed", "fb.com/madjed"),
    )

    for ar in new_artists:
        ar.save()

```

##### 2. all artists sorted by name.

code:

```python
def list_all_artists():
    for ar in Artist.objects.all():
        print(ar)

```

output:

```
artist name: artist0, social-media: fb.com/artist0
artist name: artist1, social-media: fb.com/artist1
artist name: artist2, social-media: fb.com/artist2
artist name: artist3, social-media: fb.com/artist3
artist name: artist4, social-media: fb.com/artist4
artist name: ammar, social-media: fb.com/ammardab3an
artist name: mahmoud, social-media: fb.com/mahmoud
artist name: majed, social-media: fb.com/madjed
```

##### 3. all artists whose names starts with 'a'.

code:

```python
def list_artists_start_a():
    for ar in Artist.objects.filter(name__startswith='a'):
        print(ar)

```

output:

```
artist name: artist0, social-media: fb.com/artist0
artist name: artist1, social-media: fb.com/artist1
artist name: artist2, social-media: fb.com/artist2
artist name: artist3, social-media: fb.com/artist3
artist name: artist4, social-media: fb.com/artist4
artist name: ammar, social-media: fb.com/ammardab3an
```

##### 4. create albums using two different ways.

code:

```python
def create_albums_two_ways():
    #first way
    ar_ammar = Artist.objects.get(pk="ammar")
    al0 = Album(name="ammars_first_album", artist=ar_ammar, 
                creation_date=timezone.now()-datetime.timedelta(days=1), 
                release_date=timezone.now()+datetime.timedelta(weeks=1), 
                cost=20.50)
    al0.save()
    
    #second way
    ar_ammar.album_set.create(name="ammars_second_album", 
                                creation_date=timezone.now(), 
                                release_date=timezone.now()+datetime.timedelta(days=1), 
                                cost=30.30)
    
    for al in ar_ammar.album_set.all():
        print(al)

```

output:

```
album name: ammars_first_album, artist: ammar
album name: ammars_second_album, artist: ammar
```

##### 5. latest release date album.

code:

```python
def latest_release_album():
    al = Album.objects.latest('release_date')
    print(al, al.release_date)

```

output:

```
album name: album2, artist: artist0 2022-10-28 12:03:15.661721+00:00
```

##### 6. albums released before today.

code:

```python
def list_albums_lt_today():
    albums_released_lt_today = Album.objects.filter(release_date__lt=timezone.now()).order_by('-release_date')
    for al in albums_released_lt_today:
        print(al, al.release_date.date())

```

output:

```
album name: album0, artist: artist0 2022-10-14
album name: album4, artist: artist1 2022-10-12
album name: album5, artist: artist2 2022-10-04
```

##### 6. albums released today or before today.

code:

```python
def list_albums_lte_today():
    albums_released_lte_today = Album.objects.filter(release_date__lte=timezone.now()-datetime.timedelta(days=1)).order_by('-release_date')
    for al in albums_released_lte_today:
        print(al, al.release_date.date())

```

output:

```
album name: album4, artist: artist1 2022-10-12
album name: album5, artist: artist2 2022-10-04
```

##### 7. albums total count.

code:

```python
def albums_count():
    tot_albums = Album.objects.count()
    print(tot_albums)

```

output:

```
10
```

##### 8. list all artists with their albums (1st way).

code:

```python
def list_artists_with_albums_st_way():
    for ar in Artist.objects.all():
        print(ar)
        ar_albums = ar.album_set.all()
        for al in ar_albums:
            print('\t', al.name, al.release_date.date(), al.cost)
        if not ar_albums:
            print('\t', 'no albums yet.')

```

output:

```
artist name: artist0, social-media: fb.com/artist0
	 album0 2022-10-14 10.0
	 album1 2022-10-21 10.1
	 album2 2022-10-28 10.2
artist name: artist1, social-media: fb.com/artist1
	 album3 2022-10-24 10.3
	 album4 2022-10-12 10.4
artist name: artist2, social-media: fb.com/artist2
	 album5 2022-10-04 10.5
	 album6 2022-10-15 10.6
artist name: artist3, social-media: fb.com/artist3
	 album7 2022-10-15 10.7
artist name: artist4, social-media: fb.com/artist4
	 no albums yet.
artist name: ammar, social-media: fb.com/ammardab3an
	 ammars_first_album 2022-10-21 20.5
	 ammars_second_album 2022-10-15 30.3
artist name: mahmoud, social-media: fb.com/mahmoud
	 no albums yet.
artist name: majed, social-media: fb.com/madjed
	 no albums yet.
```

##### 9. list all artists with their albums (2nd way).

code:

```python
def list_artists_with_albums_nd_way():
    for ar in Artist.objects.all():
        print(ar)
        ar_albums = Album.objects.filter(artist=ar)
        for al in ar_albums:
            print('\t', al.name, al.release_date.date(), al.cost)
        if not ar_albums:
            print('\t', 'no albums yet.')

```

output:

```
artist name: artist0, social-media: fb.com/artist0
	 album0 2022-10-14 10.0
	 album1 2022-10-21 10.1
	 album2 2022-10-28 10.2
artist name: artist1, social-media: fb.com/artist1
	 album3 2022-10-24 10.3
	 album4 2022-10-12 10.4
artist name: artist2, social-media: fb.com/artist2
	 album5 2022-10-04 10.5
	 album6 2022-10-15 10.6
artist name: artist3, social-media: fb.com/artist3
	 album7 2022-10-15 10.7
artist name: artist4, social-media: fb.com/artist4
	 no albums yet.
artist name: ammar, social-media: fb.com/ammardab3an
	 ammars_first_album 2022-10-21 20.5
	 ammars_second_album 2022-10-15 30.3
artist name: mahmoud, social-media: fb.com/mahmoud
	 no albums yet.
artist name: majed, social-media: fb.com/madjed
	 no albums yet.
```

##### 10. list all albums ordered by cost then name.

code:

```python
def list_albums_by_cost_name():
    albums_ordered_by_cost_name = Album.objects.order_by('cost', 'name')
    for al in albums_ordered_by_cost_name:
        print(al, ', cost: ', al.cost, sep='')

```

output:

```
album name: album0, artist: artist0, cost: 10.0
album name: album1, artist: artist0, cost: 10.1
album name: album2, artist: artist0, cost: 10.2
album name: album3, artist: artist1, cost: 10.3
album name: album4, artist: artist1, cost: 10.4
album name: album5, artist: artist2, cost: 10.5
album name: album6, artist: artist2, cost: 10.6
album name: album7, artist: artist3, cost: 10.7
album name: ammars_first_album, artist: ammar, cost: 20.5
album name: ammars_second_album, artist: ammar, cost: 30.3
```
