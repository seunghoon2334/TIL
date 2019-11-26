from rest_framework import serializers

from .models import Genre, Movie, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score']
        
class MovieSerializer(serializers.ModelSerializer):
    score_set = ScoreSerializer(many=True)
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
    
class ScoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'