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