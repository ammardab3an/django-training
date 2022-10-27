
from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Album(TimeStampedModel):
    
    name = models.CharField(max_length=200)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)   
    release_date = models.DateTimeField(blank=False)
    cost = models.FloatField(default=0.0, blank=False)
    is_approved = models.BooleanField("Approve the album if its name is not explicit", default=False)
    
    def __str__(self):
        return "{name}, {artist}".format(name=self.name, artist=self.artist.name)