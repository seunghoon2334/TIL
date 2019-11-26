from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views

urlpatterns = [
    path('docs/', get_swagger_view(title='음악 정보 API')),
    path('musics/', views.music_list),
    path('musics/<int:music_pk>/', views.music_detail),
    path('artist/', views.artist_list),
    path('artist/<int:artist_pk>/', views.artist_detail),
    path('musics/<int:music_pk>/comments/', views.comment_create),
    path('musics/<int:music_pk>/comments/<int:comment_pk>/', views.comment_update_delete),
]