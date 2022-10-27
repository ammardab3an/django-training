from artists.models import Artist
from albums.models import Album, Song
from django.contrib.auth.models import User

User.objects.all().delete()

User.objects.create_superuser('admin', 'admin@mail.com', 'admin')
User.objects.create_user('ammar', 'ammar@mail.com', 'ammar')
User.objects.create_user('ahmad', 'ahmad@mail.com', 'ahmad')

