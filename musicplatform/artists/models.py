from unittest.util import _MAX_LENGTH
from django.db import models

class Artist(models.Model):
    
    name = models.CharField(max_length=200, primary_key=True)
    social_media_link = models.URLField(max_length=300, blank=True, null=False)
    
    def __str__(self):
        return "artist name: {}, social-media: {}".format(self.name, self.social_media_link)