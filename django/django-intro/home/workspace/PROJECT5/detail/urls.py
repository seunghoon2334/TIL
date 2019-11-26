from django.urls import path, include
# home 폴더 내에 있는 views.py를 불러온다.
from . import views

urlpatterns = [
    path('', views.Mysite),
    path('qna/', views.QnA),
    path('mypage/', views.Mypage),
    path('signup/', views.SignUp),
]