from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.functions import Coalesce

class ArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            approved_albums=Coalesce(models.Count("album"), 0)
        )
        
class Artist(models.Model):
    
    name = models.CharField(max_length=200, primary_key=True)
    social_media_link = models.URLField(max_length=300, blank=True, null=False)
    objects = ArtistManager()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return "artist name: {}, social-media: {}".format(self.name, self.social_media_link)