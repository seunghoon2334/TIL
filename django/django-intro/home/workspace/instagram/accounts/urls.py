from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
    path('fake/', views.fake, name='fake'),
    path('visit/', views.visit, name='visit'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/', views.profile, name='profile'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('search/', views.search, name='search'),
    path('', views.userlist, name='list'),
]