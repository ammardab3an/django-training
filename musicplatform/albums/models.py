
from django.db import models

# Create your models here.

class Album(models.Model):
    
    name = models.CharField(max_length=200)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)   
    creation_date = models.DateTimeField(blank=False)
    release_date = models.DateTimeField(blank=False)
    cost = models.FloatField(default=0.0, blank=False)
    
    def __str__(self):
        return "album name: {name}, artist: {artist}".format(name=self.name, artist=self.artist.name)