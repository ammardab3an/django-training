from artists.models import Artist
from albums.models import Album, Song
from users.models import ExUser

ExUser.objects.all().delete()
ExUser.objects.create_superuser('admin', 'admin@mail.com', 'admin')
ExUser.objects.create_user('ammar', 'ammar@mail.com', 'ammar')
ExUser.objects.create_user('ahmad', 'ahmad@mail.com', 'ahmad')
