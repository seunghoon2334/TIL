# PROJECT 7 (Django - 데이터베이스 설계)

## movies

### migrations

#### 0001_initial.py

```python
# Generated by Django 2.1.5 on 2019-03-15 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [ # Genre, Movie, Score Model들을 만들어준다 
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('audience', models.IntegerField()),
                ('poster_url', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=140)),
                ('score', models.FloatField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
    ]

```

#### __init__.py

### templates

#### movies

##### base.html
```html
<!DOCTYPE html> <!-- html 파일들에 기본 base를 제공한다 -->
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

{% block body %} <!-- 영화의 세부 내용들을 보여준다 -->
<p>{{movie.id}}</p>
<p>{{movie.title}}</p>
<p>{{movie.audience}}</p>
<img src='{{movie.poster_url}}'>
<p>{{movie.description}}</p>
<p>{{movie.genre.name}}</p> <!-- movie의 genre의 이름을 보여준다 -->
<hr> <!-- 영화목록으로 돌아가기, 수정하기, 삭제하기 기능 추가 -->
<a href="{% url 'movies:index' %}">목록</a> 
<a href="{% url 'movies:edit' movie.pk %}">수정</a>
<form action="{% url 'movies:delete' movie.pk %}" method="POST" style='display: inline' onsubmit="return confirm('삭제할거야?')">
    {% csrf_token %}
    <input type='submit' value='삭제'>
</form>
<hr>
<!-- 감상평 작성 -->
<p>댓글 작성 {{ comments.count }}</p> <!-- 저장된 감상평의 갯수를 세서 나타내준다 -->
<form action="{% url 'movies:score_new' movie.pk %}" method="POST">
    {% csrf_token %} <!-- movie.pk를 통해 연결된 영화의 감상평만을 보여준다 -->
    <input type="text" name="content">
    <input type="float" name="score">
    <input type="submit">
</form>

<hr>
{% for comment in comments %} <!-- 감상평들을 for문을 통해 평점과 함께 보여준다 -->
    <li>{{ forloop.counter }} : {{ comment.content }}, {{ comment.score }}점
        <form action="{% url 'movies:score_delete' movie.pk comment.pk %}" method="POST" style="display: inline" onsubmit="return confirm('삭제할거야?')">
            {% csrf_token %}
            <input type="submit" value="삭제">
        </form>
    </li>
{% empty %} <!-- 감상평이 텅 비어있을시 나타나는 기능 -->
    <b><p>댓글이 없어요ㅠ_ㅠ</p></b>
{% endfor %}
{% endblock %}
```

##### edit.html
```html
{% extends 'movies/base.html' %}

{% block body %}
<form method='POST'>
    {% csrf_token %} <!-- POST 방식 사용시 csrf_token 필수! -->
    <input type='text' name='title' value={{movie.title}}>
    <input type='text' name='audience' value={{movie.audience}}>
    <input type='textarea' name='poster_url' value={{movie.poster_url}}>
    <input type='textarea' name='description' value={{movie.description}}>
    <input type='integer' name='genre_id' value={{movie.genre_id}}>
    <input type='submit'>
</form>
<a href="{% url 'movies:index' %}">목록</a>
{% endblock %}
```

##### index.html

```html
{% extends 'movies/base.html' %}

{% block body %}
{% for movie in movies %} <!-- 영화 제목과 포스터 url을 통한 이미지를 불러온다 -->
    <a href='{% url 'movies:detail' movie.pk %}'>{{movie.title}}</a>
    <img src='{{movie.poster_url}}'>
    <hr>
{% endfor %}
{% endblock %}
```

### __init__.py

### admin.py

```python
from django.contrib import admin
from .models import Genre,Movie,Score # models에서 Genre, Movie, Score 클래스를 import 한다
# Register your models here.
admin.site.register(Genre) # admin 사이트에 클래스를 등록한다
admin.site.register(Movie)
admin.site.register(Score)
```

### apps.py

### models.py

```python
from django.db import models

# Create your models here.

class Genre(models.Model): # 장르 클래스
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class Movie(models.Model): # 영화 클래스
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # 영화 클래스에서 장르 클래스로 연결시킨다
class Score(models.Model): # 스코어 클래스
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=140)
    score = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 스코어 클래스에서 영화 클래스로 연결시킨다
```

### tests.py

### urls.py

```python
from django.urls import path
from . import views # views의 모든걸 import 한다

app_name = 'movies' # app 이름을 movies로 설정한다

urlpatterns = [ # name을 설정하면 redirect시 name만으로 주소로 이동이 가능하다
    path('', views.index, name='index'), # 영화목록(메인화면)
    path('<int:movie_pk>', views.detail, name='detail'), # 영화상세보기
    path('<int:movie_pk>/edit/', views.edit, name='edit'), # 영화수정하기
    path('<int:movie_pk>/delete/', views.delete, name='delete'), # 영화삭제하기
    path('<int:movie_pk>/scores/new/', views.score_new, name='score_new'), # 새로운 감상평 추가하기
    path('<int:movie_pk>/scores/<int:comment_pk>/delete/', views.score_delete, name='score_delete'), # 감상평 삭제하기
]
```

### views.py

```python
from django.shortcuts import render, redirect
from .models import Genre,Movie,Score # Genre,Movie,Score 세개 클래스를 import한다 
# Create your views here.

def index(request): # 메인화면 영화목록을 보여준다
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies':movies})

def detail(request, movie_pk): # 영화 상세 페이지 index 페이지에서 movie_pk를 받아와 사용한다
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.score_set.all() # 영화의 감상평을 가져온다
    context = {
        'movie':movie,
        'comments':comments
    }
    return render(request, 'movies/detail.html', context)
    
def edit(request, movie_pk): # 영화 수정 페이지 
    if request.method == 'POST': # 수정 완료 후 상세보기 페이지로 이동
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
        
def delete(request, movie_pk): # 영화 삭제 페이지
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST': # 삭제 완료 후 영화목록 페이지로 이동
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)
    
def score_new(request, movie_pk): # 새로운 감상평 추가 페이지
    movie = Movie.objects.get(pk=movie_pk) # 연결된 영화의 정보를 가져온다
    comment = Score() # Score 클래스의 comment를 새로 만든다
    comment.content = request.POST.get('content')
    comment.score = request.POST.get('score')
    comment.movie = movie
    comment.save()
    return redirect('movies:detail', movie.pk)
    
def score_delete(request, movie_pk, comment_pk): # 감상평 삭제 페이지
    if request.method == "POST": # 삭제 완료 후 상세보기 페이지로 이동
        comment = Score.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('movies:detail', movie_pk)
```

## PROJECT7

### __init__.py

### settings.py

```python
ALLOWED_HOSTS = ['*'] # 전체 허용! *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies', # movies라는 앱을 추가한다.
]

LANGUAGE_CODE = 'ko-kr' #한국어버전

TIME_ZONE = 'Asia/Seoul' #시간을 아시아/서울로 변경
```

### urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')), # url에 movies를 포함시킨다.
]
```

### wsgi.py

## db.sqlite3

## genre.csv

```genre.csv
id,
1,가족
2,공포(호러)
3,드라마
4,멜로/로맨스
5,미스터리
6,사극
7,스릴러
8,액션
9,어드벤처
10,판타지
11,코미디
```

## manage.py

## movie.csv

```
id,title,audience,poster_url,description,genre_id
1,캡틴 마블,3035808,https://ssl.pstatic.net/imgmovie/mdi/mit110/1326/132623_P22_133853.jpg,"1995년, 공군 파일럿 시절의 기억을 잃고 크리족 전사로 살아가던 캐럴 댄버스(브리 라슨)가 지구에 불시착한다. 쉴드 요원 닉 퓨리(사무엘 L. 잭슨)에게 발견되어 팀을 이룬 그들은 지구로 향하는 더 큰 위협을 감지하고 힘을 합쳐 전쟁을 끝내야 하는데...",9
2,항거:유관순 이야기,1041939,https://ssl.pstatic.net/imgmovie/mdi/mit110/1823/182360_P11_140223.jpg,"1919년 3.1 만세운동 후 세평도 안 되는 서대문 감옥 8호실 속, 영혼만은 누구보다 자유로웠던 유관순과 8호실 여성들의 1년의 이야기.",3
3,사바하,2340441,https://ssl.pstatic.net/imgmovie/mdi/mit110/1670/167099_P13_101134.jpg,"사람들은 말했다. 그때, 그냥, 그것이 죽었어야 한다고… 한 시골 마을에서 쌍둥이 자매가 태어난다. 온전치 못한 다리로 태어난 ‘금화’(이재인)와 모두가 오래 살지 못할 것이라고 했던 언니 ‘그것’. 그것이 태어나고 모든 사건이 시작되었다.",5
4,증인,2457258,https://ssl.pstatic.net/imgmovie/mdi/mit110/1773/177374_P100_112832.jpg,신념은 잠시 접어두고 현실을 위해 속물이 되기로 마음먹은 민변 출신의 대형 로펌 변호사 ‘순호’(정우성). 파트너 변호사로 승진할 수 있는 큰 기회가 걸린 사건의 변호사로 지목되자 살인 용의자의 무죄를 입증하기 위해 유일한 목격자인 자폐 소녀 ‘지우’(김향기)를 증인으로 세우려 한다.,3
5,극한직업,16178563,https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167651_P106_141030.jpg,"불철주야 달리고 구르지만 실적은 바닥, 급기야 해체 위기를 맞는 마약반! 더 이상 물러설 곳이 없는 팀의 맏형 고반장은 국제 범죄조직의 국내 마약 밀반입 정황을 포착하고 장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다.",11
6,그린 북,372293,https://ssl.pstatic.net/imgmovie/mdi/mit110/1715/171539_P26_135622.jpg,"1962년 미국, 입담과 주먹만 믿고 살아가던 토니 발레롱가(비고 모텐슨)는 교양과 우아함 그 자체인 천재 피아니스트 돈 셜리(마허샬라 알리) 박사의 운전기사 면접을 보게 된다. 백악관에도 초청되는 등 미국 전역에서 콘서트 요청을 받으며 명성을 떨치고 있는 돈 셜리는 위험하기로 소문난 미국 남부 투어 공연을 떠나기로 결심하고...",3
7,더 페이버릿: 여왕의 여자,133508,https://ssl.pstatic.net/imgmovie/mdi/mit110/1489/148909_P29_164758.jpg,절대 권력을 지닌 히스테릭한 영국의 여왕 ‘앤’(올리비아 콜맨). 여왕의 오랜 친구이자 권력의 실세 ‘사라 제닝스’(레이첼 와이즈)와 신분 상승을 노리는 몰락한 귀족 가문 출신의 욕망 하녀 ‘애비게일 힐’(엠마 스톤)은 여왕의 총애를 받기 위해 수단과 방법을 가리지 않고 발버둥치기 시작하는데…,3
8,리노,16489,https://ssl.pstatic.net/imgmovie/mdi/mit110/1709/170953_P08_140411.jpg,"못생긴 고양이 분장 전문 파티 플래너 ‘리노’는 소심한 성격에 되는 일 하나 없는 불만 가득 청년. 하루하루 무기력하게 살아가던 중 우연히 광고를 보고 찾아간 마법사 ‘돈 레옹’에게 자신의 인생을 변화시켜 줄 것을 요청하지만 마법사의 실수로 진짜 고양이로 변하게 된다. 귀엽고 커다란 고양이의 모습에 난생 처음으로 사람들의 관심을 한 몸에 받지만, 얼마 안 가 인생 최대의 위기를 맞게 되는데...",9
9,자전차왕 엄복동,168860,https://ssl.pstatic.net/imgmovie/mdi/mit110/1590/159070_P13_114738.jpg,"일제강점기, 일본에서는 조선의 민족의식을 꺾고 그들의 지배력을 과시하기 위해 전조선자전차대회를 개최한다. 하지만 일본 최고의 선수들을 제치고 조선인 최초로 우승을 차지한 엄복동의 등장으로 일본의 계략은 실패로 돌아가고...",3
10,신데렐라:마법 반지의 비밀,281692,https://ssl.pstatic.net/imgmovie/mdi/mit110/1819/181959_P11_114544.jpg,"새어머니와 두 언니들의 구박에도 늘 씩씩하고 당찬 신데렐라는 왕궁 무도회에 가보고 싶다는 생쥐 친구들의 소원을 들어주기 위해 무도회 참석을 결정하지만 누더기 옷 때문에 고민에 빠지고 꼬꼬마 마법사 크리스탈을 찾아가 도움을 청한다. 이에 마법사 크리스탈은 신데렐라를 아름답게 치장하고, 생쥐 친구들을 화려한 황금 마차를 모는 멋진 말들로 변신시키는데...",10
```

