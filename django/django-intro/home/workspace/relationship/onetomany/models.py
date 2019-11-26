from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    
class Post(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Comment(models.Model):
    content = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
