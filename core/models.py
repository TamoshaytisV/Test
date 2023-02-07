from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Song(models.Model):
    title = models.CharField(max_length=255)
    length = models.CharField(max_length=6)
    album = models.ForeignKey(Album, related_name="songs", on_delete=models.DO_NOTHING)