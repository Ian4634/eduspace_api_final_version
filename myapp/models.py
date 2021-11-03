from django.db import models

# Create your models here.
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=1000)
    source = models.URLField(blank = True)
    descriptions = models.CharField(blank=True, max_length=1500)