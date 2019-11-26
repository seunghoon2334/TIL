from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('make/', views.make, name='make'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/delete', views.delete, name='delete'),
    path('<int:post_pk>/edit', views.edit, name='edit'),
    path('<int:post_pk>/comment_create', views.comment_create, name='comment_create'),
    path('<int:post_pk>/<int:comment_pk>/comments_delete', views.comments_delete, name='comments_delete'),
    path('<int:post_pk>/like', views.like, name='like'),
    path('hashtags/<int:hashtag_pk>', views.hashtag, name='hashtag'),
]