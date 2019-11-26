from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Genre,Movie,Score
# Create your views here.

def index(request):
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    return render(request, 'movies/index.html', {'movies':movies})

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.score_set.all()
    context = {
        'movie':movie,
        'comments':comments
    }
    return render(request, 'movies/detail.html', context)
    
def edit(request, movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.genre = request.POST.get('genre')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        movie = Movie.objects.get(pk=movie_pk)
        return render(request, 'movies/edit.html', {'movie':movie})
        
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)
    
def score_new(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment = Score()
    comment.content = request.POST.get('content')
    comment.score = request.POST.get('score')
    comment.movie = movie
    comment.save()
    return redirect('movies:detail', movie.pk)
    
def score_delete(request, movie_pk, comment_pk):
    if request.method == "POST":
        comment = Score.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('movies:detail', movie_pk)