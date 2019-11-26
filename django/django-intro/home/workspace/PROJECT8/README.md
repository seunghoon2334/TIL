# PROJECT8

## movies

### fixtures

#### genre.json

#### movie.json

### migrations

#### 0001_initial.py

#### __init__.py

### templates

#### movies

##### base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

##### detail.html

```html
{% extends 'movies/base.html' %}

{% block body %}
<p>{{movie.id}}</p>
<p>{{movie.title}}</p>
<p>{{movie.audience}}</p>
<img src='{{movie.poster_url}}'>
<p>{{movie.description}}</p>
<p>{{movie.genre.name}}</p>
<hr>
<a href="{% url 'movies:index' %}">목록</a>
<a href="{% url 'movies:update' movie.pk %}">수정</a>
<form action="{% url 'movies:delete' movie.pk %}" method="POST" style='display: inline' onsubmit="return confirm('삭제할거야?')">
    {% csrf_token %}
    <input type='submit' value='삭제'>
</form>
<hr>

<p>댓글 작성 {{ scores.count }}</p>
<form action="{% url 'movies:score_create' movie.pk %}" method="POST">
    {% csrf_token %}
    <input type="text" name="content">
    <input type="float" name="score">
    <input type="submit">
</form>

<hr>
{% for score in scores %}
    <li>{{ forloop.counter }} : {{ score.content }}, {{ score.score }}점
        <form action="{% url 'movies:score_delete' movie.pk score.pk %}" method="POST" style="display: inline" onsubmit="return confirm('삭제할거야?')">
            {% csrf_token %}
            <input type="submit" value="삭제">
        </form>
    </li>
{% empty %}
    <b><p>댓글이 없어요ㅠ_ㅠ</p></b>
{% endfor %}
{% endblock %}
```

##### form.html

```html
{% extends 'movies/base.html' %}
{% block body %}
{% load crispy_forms_tags %}
{% if request.resolver_match.url_name == 'create' %}
    <h1>글 생성</h1>
{% else %}
    <h1>글 수정</h1>
{% endif %}
<form method='POST'>
    {% csrf_token %}
    {{ movie_form|crispy }}
    <input type='submit'>
</form>

{% endblock %}
```

##### index.html

```html
{% extends 'movies/base.html' %}

{% block body %}
<a href="{% url 'movies:create' %}"><h1>new</h1></a>
<hr>
{% for movie in movies %}
    <a href='{% url 'movies:detail' movie.pk %}'>{{movie.title}}</a>
    <p> {{ movie.score_avg }} </p>
    <img src='{{movie.poster_url}}'>
    <hr>
{% endfor %}
{% endblock %}
```

### __init__.py

### admin.py

```python
from django.contrib import admin
from .models import Genre,Movie,Score
# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Score)
```

### apps.py

### forms.py

```python
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Movie

# modelform
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.add_input(Submit('Submit', '제출!'))
```

### models.py

```python
from django.db import models
from django.urls import reverse
# Create your models here.

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('movies:detail', args=[self.pk])
    
class Score(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=140)
    score = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
```

### tests.py

### urls.py

```python
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:movie_pk>', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('<int:movie_pk>/edit/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/scores/new/', views.score_create, name='score_create'),
    path('<int:movie_pk>/scores/<int:score_pk>/delete/', views.score_delete, name='score_delete'),
]
```

### views.py

```python
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
```

## PROJECT8

### __init__.py

### settings.py

```python
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'movies',
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```



### urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]
```

### wsgi.py

## db.sqlite3

## manage.py







* 데이터 업로드 하기

python manage.py loaddata genre.json

python manage.py loaddata movie.json

```
PROJECT8 

|___movies

	|___fixtures

		|___genre.json

		|___movie.json
```



