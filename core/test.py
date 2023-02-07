import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'mutant.settings'
django.setup()

from core.models import Album


def test(request):
    albums = Album.objects.all()
    print(albums)

test()