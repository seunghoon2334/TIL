from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music, Artist, Comment
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
# Create your views here.

@api_view(['GET'])
def music_list(request):
    '''
    음악 정보 출력
    '''
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def music_detail(request, music_pk):
    '''
    음악 상세 보기
    '''
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
    
@api_view(['GET'])
def artist_list(request):
    '''
    아티스트 정보 출력
    '''
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def artist_detail(request, artist_pk):
    '''
    아티스트 상세 보기
    '''
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)
    
@api_view(['POST'])
def comment_create(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music=music)
        return Response(serializer.data)

@api_view(['DELETE', 'PUT'])
def comment_update_delete(request, music_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '성공적으로 수정되었습니다.'})
    else:
        comment.delete()
        return Response({'message': f'음악 {music_pk}의 댓글이 삭제되었습니다.'})