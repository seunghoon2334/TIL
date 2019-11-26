from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Genre, Movie, Score
# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request, 'movies/list.html', context)
    
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    scores = movie.score_set.all()
    context = {'movie':movie, 'scores':scores}
    return render(request, 'movies/detail.html', context)

@login_required
def score_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    score = Score()
    score.content = request.POST.get('content')
    score.value = request.POST.get('value')
    score.movie = movie
    score.user = request.user
    score.save()
    return redirect('movies:detail', movie_pk)
    
def score_delete(request, movie_pk, score_pk):
    if request.method == "POST":
        score = Score.objects.get(pk=score_pk)
        score.delete()
    return redirect('movies:detail', movie_pk)