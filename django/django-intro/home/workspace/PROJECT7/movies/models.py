from django.db import models

# Create your models here.

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class Score(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=140)
    score = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)