from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Genre,Movie,Score
from .forms import MovieForm
# Create your views here.

def index(request):
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    return render(request, 'movies/index.html', {'movies':movies})

def create(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect(movie)
    else:
        movie_form = MovieForm()
    context = {'movie_form': movie_form}
    return render(request, 'movies/form.html', context)
    
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    scores = movie.score_set.all()
    context = {
        'movie':movie,
        'scores':scores
    }
    return render(request, 'movies/detail.html', context)
    
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect(movie)
    else:
        movie_form = MovieForm(instance=movie)
    context = {'movie_form': movie_form}
    return render(request, 'movies/form.html', context)
        
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect(movie)
    
def score_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    score = Score()
    score.content = request.POST.get('content')
    score.score = request.POST.get('score')
    score.movie = movie
    score.save()
    return redirect('movies:detail', movie.pk)
    
def score_delete(request, movie_pk, score_pk):
    if request.method == "POST":
        score = Score.objects.get(pk=score)
        score.delete()
    return redirect('movies:detail', movie_pk)