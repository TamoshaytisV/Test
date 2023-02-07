from django.db import models



class Ninja(models.Model):
    name = models.CharField(max_length=10)
