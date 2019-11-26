from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

class Hashtag(models.Model):
    content = models.TextField(unique=True)

class Post(models.Model):
    content = models.TextField()
    # image = models.ImageField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts')
    hashtags = models.ManyToManyField(Hashtag, blank=True, related_name='posts')
    
    @property
    def like_count(self):
        return self.liked_users.count()
    
    def __str__(self):
        return f'Post : {self.pk} '
        
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.pk])
            
class Image(models.Model):
    file = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
        
class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.content