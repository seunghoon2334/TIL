from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    option_A = models.CharField(max_length=50)
    option_B = models.CharField(max_length=50)
    
class Answer(models.Model):
    user = models.CharField(max_length=10)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
class Count(models.Model):
    count = models.CharField(max_length=10)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    