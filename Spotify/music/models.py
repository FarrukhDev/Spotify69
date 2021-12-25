from django.db import models

class Artist(models.Model):
    name=models.CharField(max_length=20)
    photo=models.URLField()
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
class Album(models.Model):
    name=models.CharField(max_length=20)
    cover=models.URLField()
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}({self.artist})"
class Song(models.Model):
    name=models.CharField(max_length=20)
    cover=models.URLField()
    source=models.URLField()
    lyrics=models.TextField()
    duration=models.DurationField()
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}  ({self.album})"


