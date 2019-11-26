from rest_framework import serializers

from .models import Music, Artist, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content']
        
class MusicSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist_name', 'comment_set']
    
class ArtistSerializer(serializers.ModelSerializer):
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'music_count']
        
class ArtistDetailSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(source='music_set', many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'musics']