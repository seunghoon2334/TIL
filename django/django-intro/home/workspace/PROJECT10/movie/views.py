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
        return Response(serializer.data)
        
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
        return Response({})