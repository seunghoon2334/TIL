# movie_pjt

## accounts

### migrations

#### 0001_initial.py

#### 0002_user_followers.py

#### __init__.py

### templates

#### accounts

##### detail.html

```html
{% extends 'base.html' %}
{% block body %}
    <h2>유저 정보</h2>
    <p>{{ user_info.username }}</p>
    <p>팔로잉 : {{ user_info.followings.all.count }}</p> <!--유저가 팔로잉/워한 유저들 수-->
    <p>팔로워 : {{ user_info.followers.all.count }}</p>
    {% if user != user_info %} <!--유저가 자기자신 팔로우를 못하게 -->
        {% if user in user_info.followers.all %}
            <a href='{% url "accounts:follow" user_info.pk%}'>팔로우취소</a>
        {% else %}
            <a href='{% url "accounts:follow" user_info.pk%}'>팔로우</a>
        {% endif %}
    {% endif %}
    <h2>영화추천</h2>
    <h3>팔로우 평점 1등</h3>
    {% for scoref in score_following %} <!--팔로우한 유저들의 평점 정보 중에 가장 높은 평점-->
        <h4>{{ scoref.user }}</h4>
        <p>{{ scoref.content }}</p>
        <p>{{ scoref.value }}</p>
        <p>{{ scoref.movie.title }}</p>
        <hr>
    {% endfor %}
    <h3>전체 평점 1등</h3> <!-- 전체 평점 중에 가장 높은 평점 -->
    <h4>{{ score_one.user }}</h4>
    <p>{{ score_one.content }}</p>
    <p>{{ score_one.value }}</p>
    <p>{{ score_one.movie.title }}</p>
    <h2>내가 작성한 평점</h2>
    {% for score in scores %}
        <hr>
        <p>{{ score.content }}</p>
        <p>{{ score.value }}</p>
        <p>{{ score.movie.title }}</p>
    {% endfor %}
{% endblock %}
```

##### forms.html

```html
{% extends 'base.html' %}
{% block body %}
<form method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="!">
</form>
{% endblock %}
```

##### list.html

```html
{% extends 'base.html' %}
{% block body %}
{% for user in users %}
    <a href='{% url "accounts:detail" user.pk %}'>{{ user.username }}</a><br>
{% endfor %}
{% endblock %}
```

### __init__.py

### admin.py

```python
from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.

admin.site.register(get_user_model())
```

### apps.py

### forms.py

```python
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)
```

### models.py

```python
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser): # M:N
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
```

### tests.py

### urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

### views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import User
from movies.models import Score
from .forms import UserCustomCreationForm

# Create your views here.
def list(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'accounts/list.html', context)
    
def detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    scores = user.score_set.all()
    score_one = Score.objects.order_by('-value')[0]
    followings = user.followings.all()
    score_following = []
    for following in followings: # 팔로잉한 유저들의 점수 중 가장 높은거 하나씩 저장
        if Score.objects.filter(user=following):
            score_following.append(Score.objects.filter(user=following).order_by('-value')[0])
    context = {'user_info':user, 'scores':scores, 'score_one':score_one, 'score_following':score_following}
    return render(request, 'accounts/detail.html', context)
    
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
@login_required    
def follow(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
        
    return redirect('accounts:detail', user_pk)
```

## movie_pjt

### templates

#### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <a href="{% url 'movies:list' %}">영화보기</a>
    <a href="{% url 'accounts:list' %}">유저보기</a>
    {% if user.is_authenticated %}
        <p>{{ user.username }}</p>
        <a href="{% url 'accounts:detail' user.pk %}">유저정보</a>
        <a href="{% url 'accounts:logout' %}">로그아웃</a>
        {% else %}
        <a href="{% url 'accounts:signup' %}">회원가입</a>
        <a href="{% url 'accounts:login' %}">로그인</a>
    {% endif %}
    <hr> 
    {% block body %}
    {% endblock %}
</body>
</html>
```

### __init__.py

### settings.py

```python
"""
Django settings for movie_pjt project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mkr$=t0@u5g9gf(=6gpxzu@)%=544by79j#azuq&50$q89e$9$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'movies',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movie_pjt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'movie_pjt', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'movie_pjt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'accounts.User'
```

### urls.py

```python
"""movie_pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
]

```

### wsgi.py

## movies

### fixtures

#### genre.json

#### movie.json

### migrations

#### 0001_initial.py

#### 0002_auto_201

##### __init__.py

### templates

#### movies

##### detail.html

```html
{% extends 'base.html' %}
{% block body %}
    <p>{{ movie.title }}</p>
    <p>{{ movie.audience }}</p>
    <img src='{{ movie.poster_url }}'>
    <p>{{ movie.description }}</p>
    <p>{{ movie.genre.name }}</p>
    <p>댓글 작성 {{ scores.count }}</p>
    <form action="{% url 'movies:score_create' movie.pk %}" method="POST">
        {% csrf_token %}
        내용 : <input type="text" name="content"><br>
        점수 : <input type="integer" name="value"><br>
        <input type="submit">
    </form>
    <hr>
    {% for score in scores %}
        <li>{{ score.user }}, {{ score.value }}점: {{ score.content }}
            {% if score.user == user %}
            <form action="{% url 'movies:score_delete' movie.pk score.pk %}" method="POST" style="display: inline" onsubmit="return confirm('삭제할거야?')">
                {% csrf_token %}
                <input type="submit" value="삭제">
            </form>
            {% endif %}
        </li>
    {% endfor %}
{% endblock %}
```

##### list.html

```html
{% extends 'base.html' %}
{% block body %}
<h1>Movies List</h1>
{% for movie in movies %}
    <a href='{% url "movies:detail" movie.pk %}'><img src='{{ movie.poster_url }}'%}></a><br>
{% endfor %}
{% endblock %}
```

### __init__.py

### admin.py

```python
from django.contrib import admin
from .models import Genre,Movie,Score
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','audience','poster_url','description','genre',)
    
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('content','value','movie','user',)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Score, ScoreAdmin)
```

### apps.py

### models.py

```python
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
```

### tests.py

### urls.py

```python
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:movie_pk>', views.detail, name='detail'),
    path('<int:movie_pk>/scores/new', views.score_create, name='score_create'),
    path('<int:movie_pk>/scores/<int:score_pk>/delete', views.score_delete, name='score_delete'),
]

```

### views.py

```python
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
```

## db.sqlite3

## manage.py

