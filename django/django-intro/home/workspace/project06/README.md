# project06

## movies

### __pycache__

### migrations

#### __pycache__

##### 0001_initial.py

##### __init__.py

### templates

#### movies

##### edit.html

```html
<form action="/movies/{{movie.pk}}/update/" method="POST">
    {% csrf_token %} <!--POST방식을 사용하기 위해 필수-->
    영화명<input type="text" name="title" value={{ movie.title }}><br>
    누적 관객수<input type="integer" name="audience" value={{ movie.audience }}><br>
    장르<input type="text" name="genre" value={{ movie.genre }}><br>
    평점<input type="float" name="score" value={{ movie.score }}><br>
    포스터 이미지 URL<textarea name="poster_url">{{ movie.poster_url }}</textarea>
    영화 소개<textarea name="description">{{ movie.description }}</textarea>
    <input type=submit>
</form> <!--pk값에 해당하는 영화 내용을 가져와서 수정한다-->
```

##### index.html

```html
{% for movie in movies %} <!--메인 페이지(영화 제목평점)-->
    <a href='{{movie.pk}}'>{{ movie.title }}</a>
    <p>{{ movie.score }}</p>
    <hr>
{% endfor %}
<a href="new/">새 영화</a>
```

##### infor.html

```html
<p>{{ movie.title }}</p> <!--movie의 내용들을 보여준다-->
<p>{{ movie.audience }}</p>
<p>{{ movie.genre }}</p>
<p>{{ movie.score }}</p>
<img src="{{movie.poster_url}}" width=40%, height=40%>
<p>{{ movie.description }}</p>
<a href="/movies/">목록</a>
<a href="edit/">수정</a>
<a href="delete/">삭제</a>
```

##### new.html

```html
<form action="/movies/create/" method="POST">
    {% csrf_token %}
    영화명<input type="text" name="title"><br>
    누적 관객수<input type="integer" name="audience"><br>
    장르<input type="text" name="genre"><br>
    평점<input type="float" name="score"><br>
    포스터 이미지 URL<textarea name="poster_url"></textarea>
    영화 소개<textarea name="description"></textarea>
    <input type=submit>
</form> <!--내용을 input타입으로 받는다-->
```

### __init__.py

### admin.py

### apps.py

### models.py

```python
from django.db import models

# Create your models here.
class Movie(models.Model): # 클래스를 만들고 내용들을 추가한다
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    genre = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
```

### tests.py

### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [ # 사용하려는 url 주소를 등록한다
    path('', views.index),
    path('<int:pk>/', views.infor),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
    path('<int:pk>/delete/', views.delete),
]
```

### views.py

```python
from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.
def index(request): # 처음 기본 화면 영화이름과 평점 보여줌
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies':movies})
    
def infor(request, pk): # pk값에 해당하는 테이블 내용을 보여줌
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/infor.html', {'movie':movie})
    
def new(request): # 새로운 내용 추가
    return render(request, 'movies/new.html')
    
def create(request): # new에서 보낸 내용을 저장 등록
    movie = Movie()
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    return redirect('/movies')
    
def edit(request, pk): # pk값에 해당하는 테이블 내용을 가져와 수정
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/edit.html', {'movie':movie})
    
def update(request, pk): # edit에서 수정한 내용을 덮어씌운후 저장
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    return redirect(f'/movies/{movie.id}')
    
def delete(render, pk): #pk값에 해당하는 테이블 내용을 가져와 삭제
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('/movies')
```

## project06

### __pycache__

### __init__.py

### settings.py

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'eem$&lgdnaow8y!)c&hc0c!)9p3feay3yrb*_#tf)l%zvgsnr+'

DEBUG = True

ALLOWED_HOSTS = ['*'] #필수 '*'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies',
] #꼭 여기에 등록을 해줘야 사용가능

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project06.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project06.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'ko_kr' #한국어버전

TIME_ZONE = 'Asia/Seoul' #기본시간은 아시아/서울

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

```

### urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')), # movies라는 url 등록
]
```

### wsgi.py

