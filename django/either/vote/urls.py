from django.urls import path
from . import views

app_name = 'vote'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:question_pk>', views.detail, name="detail"),
    path('<int:question_pk>/select', views.select, name="select"),
    path('<int:question_pk>/comment/', views.create_comment, name="create_comment"),
]