from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    score_users = models.ManyToManyField(
                                    settings.AUTH_USER_MODEL, 
                                    through='Score', 
                                    related_name='score_movies'
                                    )

class Score(models.Model):
    content = models.CharField(max_length=140)
    value = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)