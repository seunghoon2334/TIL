# PROJECT10

## movie

### fixtures

#### genre.json

![/PROJECT10/movie/static/docs](image/PROJECT10/movie/static/docs.png)

````json
[
    {
        "pk": 1,
        "model": "movie.genre",
        "fields": {
            "name": "가족"
        }
    },
    {
        "pk": 2,
        "model": "movie.genre",
        "fields": {
            "name": "공포(호러)"
        }
    },
    {
        "pk": 3,
        "model": "movie.genre",
        "fields": {
            "name": "드라마"
        }
    },
    {
        "pk": 4,
        "model": "movie.genre",
        "fields": {
            "name": "멜로/로맨스"
        }
    },
    {
        "pk": 5,
        "model": "movie.genre",
        "fields": {
            "name": "미스터리"
        }
    },
    {
        "pk": 6,
        "model": "movie.genre",
        "fields": {
            "name": "사극"
        }
    },
    {
        "pk": 7,
        "model": "movie.genre",
        "fields": {
            "name": "스릴러"
        }
    },
    {
        "pk": 8,
        "model": "movie.genre",
        "fields": {
            "name": "액션"
        }
    },
    {
        "pk": 9,
        "model": "movie.genre",
        "fields": {
            "name": "어드벤처"
        }
    },
    {
        "pk": 10,
        "model": "movie.genre",
        "fields": {
            "name": "판타지"
        }
    },
    {
        "pk": 11,
        "model": "movie.genre",
        "fields": {
            "name": "코미디"
        }
    }
]
````

#### movis.json

```json
[
    {
        "pk": 1,
        "model": "movie.movie",
        "fields": {
            "title": "캡틴 마블",
            "audience": 3035808,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1326/132623_P22_133853.jpg",
            "description": "1995년, 공군 파일럿 시절의 기억을 잃고 크리족 전사로 살아가던 캐럴 댄버스(브리 라슨)가 지구에 불시착한다. 쉴드 요원 닉 퓨리(사무엘 L. 잭슨)에게 발견되어 팀을 이룬 그들은 지구로 향하는 더 큰 위협을 감지하고 힘을 합쳐 전쟁을 끝내야 하는데...",
            "genre_id": 9
        }
    },
    {
        "pk": 2,
        "model": "movie.movie",
        "fields": {
            "title": "항거:유관순 이야기",
            "audience": 1041939,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1823/182360_P11_140223.jpg",
            "description": "1919년 3.1 만세운동 후 세평도 안 되는 서대문 감옥 8호실 속, 영혼만은 누구보다 자유로웠던 유관순과 8호실 여성들의 1년의 이야기.",
            "genre_id": 3
        }
    },
    {
        "pk": 3,
        "model": "movie.movie",
        "fields": {
            "title": "사바하",
            "audience": 2340441,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1670/167099_P13_101134.jpg",
            "description": "사람들은 말했다. 그때, 그냥, 그것이 죽었어야 한다고… 한 시골 마을에서 쌍둥이 자매가 태어난다. 온전치 못한 다리로 태어난 ‘금화’(이재인)와 모두가 오래 살지 못할 것이라고 했던 언니 ‘그것’. 그것이 태어나고 모든 사건이 시작되었다.",
            "genre_id": 5
        }
    },
    {
        "pk": 4,
        "model": "movie.movie",
        "fields": {
            "title": "증인",
            "audience": 2457258,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1773/177374_P100_112832.jpg",
            "description": "신념은 잠시 접어두고 현실을 위해 속물이 되기로 마음먹은 민변 출신의 대형 로펌 변호사 ‘순호’(정우성). 파트너 변호사로 승진할 수 있는 큰 기회가 걸린 사건의 변호사로 지목되자 살인 용의자의 무죄를 입증하기 위해 유일한 목격자인 자폐 소녀 ‘지우’(김향기)를 증인으로 세우려 한다.",
            "genre_id": 3
        }
    },
    {
        "pk": 5,
        "model": "movie.movie",
        "fields": {
            "title": "극한직업",
            "audience": 16178563,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167651_P106_141030.jpg",
            "description": "불철주야 달리고 구르지만 실적은 바닥, 급기야 해체 위기를 맞는 마약반! 더 이상 물러설 곳이 없는 팀의 맏형 고반장은 국제 범죄조직의 국내 마약 밀반입 정황을 포착하고 장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다.",
            "genre_id": 11
        }
    },
    {
        "pk": 6,
        "model": "movie.movie",
        "fields": {
            "title": "그린 북",
            "audience": 372293,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1715/171539_P26_135622.jpg",
            "description": "1962년 미국, 입담과 주먹만 믿고 살아가던 토니 발레롱가(비고 모텐슨)는 교양과 우아함 그 자체인 천재 피아니스트 돈 셜리(마허샬라 알리) 박사의 운전기사 면접을 보게 된다. 백악관에도 초청되는 등 미국 전역에서 콘서트 요청을 받으며 명성을 떨치고 있는 돈 셜리는 위험하기로 소문난 미국 남부 투어 공연을 떠나기로 결심하고...",
            "genre_id": 3
        }
    },
    {
        "pk": 7,
        "model": "movie.movie",
        "fields": {
            "title": "더 페이버릿: 여왕의 여자",
            "audience": 133508,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1489/148909_P29_164758.jpg",
            "description": "절대 권력을 지닌 히스테릭한 영국의 여왕 ‘앤’(올리비아 콜맨). 여왕의 오랜 친구이자 권력의 실세 ‘사라 제닝스’(레이첼 와이즈)와 신분 상승을 노리는 몰락한 귀족 가문 출신의 욕망 하녀 ‘애비게일 힐’(엠마 스톤)은 여왕의 총애를 받기 위해 수단과 방법을 가리지 않고 발버둥치기 시작하는데…",
            "genre_id": 3
        }
    },
    {
        "pk": 8,
        "model": "movie.movie",
        "fields": {
            "title": "리노",
            "audience": 16489,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1709/170953_P08_140411.jpg",
            "description": "못생긴 고양이 분장 전문 파티 플래너 ‘리노’는 소심한 성격에 되는 일 하나 없는 불만 가득 청년. 하루하루 무기력하게 살아가던 중 우연히 광고를 보고 찾아간 마법사 ‘돈 레옹’에게 자신의 인생을 변화시켜 줄 것을 요청하지만 마법사의 실수로 진짜 고양이로 변하게 된다. 귀엽고 커다란 고양이의 모습에 난생 처음으로 사람들의 관심을 한 몸에 받지만, 얼마 안 가 인생 최대의 위기를 맞게 되는데...",
            "genre_id": 9
        }
    },
    {
        "pk": 9,
        "model": "movie.movie",
        "fields": {
            "title": "자전차왕 엄복동",
            "audience": 168860,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1590/159070_P13_114738.jpg",
            "description": "일제강점기, 일본에서는 조선의 민족의식을 꺾고 그들의 지배력을 과시하기 위해 전조선자전차대회를 개최한다. 하지만 일본 최고의 선수들을 제치고 조선인 최초로 우승을 차지한 엄복동의 등장으로 일본의 계략은 실패로 돌아가고...",
            "genre_id": 3
        }
    },
    {
        "pk": 10,
        "model": "movie.movie",
        "fields": {
            "title": "신데렐라:마법 반지의 비밀",
            "audience": 281692,
            "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1819/181959_P11_114544.jpg",
            "description": "새어머니와 두 언니들의 구박에도 늘 씩씩하고 당찬 신데렐라는 왕궁 무도회에 가보고 싶다는 생쥐 친구들의 소원을 들어주기 위해 무도회 참석을 결정하지만 누더기 옷 때문에 고민에 빠지고 꼬꼬마 마법사 크리스탈을 찾아가 도움을 청한다. 이에 마법사 크리스탈은 신데렐라를 아름답게 치장하고, 생쥐 친구들을 화려한 황금 마차를 모는 멋진 말들로 변신시키는데...",
            "genre_id": 10
        }
    }
]
```

### migrations

#### 0001_initial.py

#### __init__.py

### __init__.py

### admin.py

```python
from django.contrib import admin

from .models import Genre, Movie, Score
# Register your models here.

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Score)
```

### apps.py

### models.py

```python
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.TextField()
    
class Movie(models.Model):
    title = models.TextField()
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Score(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
```

### serializers.py

```python
from rest_framework import serializers

from .models import Genre, Movie, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(source='movie_set', many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'movies', 'name']
        
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score']
    
class ScoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'
```

### tests.py

### urls.py

```python
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views

urlpatterns = [
    path('docs/', get_swagger_view(title='영화 정보 API')),
    path('genres/', views.genre_list),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/scores/', views.score_create),
    path('scores/<int:score_pk>/', views.score_detail_update_delete),
]
```

### views.py

```python
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Score
from .serializers import GenreSerializer, GenreDetailSerializer, MovieSerializer, MovieDetailSerializer, ScoreSerializer, ScoreDetailSerializer
# Create your views here.

@api_view(['GET'])
def genre_list(request):
    '''
    장르 정보 출력
    '''
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genre_detail(request, genre_pk):
    '''
    장르 상세 보기
    '''
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_list(request):
    '''
    영화 정보 출력
    '''
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    '''
    영화 상세 보기
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)
    
@api_view(['POST'])
def score_create(request, movie_pk):
    '''
    평점 생성 하기
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response({'message': f'작성되었습니다.'})
        
@api_view(['GET', 'PUT', 'DELETE'])
def score_detail_update_delete(request, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    if request.method == 'GET':
        '''
        평점 상세 보기
        '''
        serializer = ScoreDetailSerializer(score)
        return Response(serializer.data)
    elif request.method == 'PUT':
        '''
        평점 수정 하기
        '''
        serializer = ScoreSerializer(data=request.data, instance=score)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': f'수정되었습니다.'})
    else:
        '''
        평점 삭제 하기
        '''
        score.delete()
        return Response({'message': f'삭제되었습니다.'})
```

## PROJECT10

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
    'rest_framework',
    'rest_framework_swagger',
    'movie',
]

```

### urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movie.urls')),
]

```

### wsgi.py

## db.sqlite3

## manage.py

