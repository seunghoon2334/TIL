from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import User
from movies.models import Score
from .forms import UserCustomCreationForm

# Create your views here.
def list(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'accounts/list.html', context)
    
from django.db.models import Prefetch
def detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    scores = user.score_set.all()
    score_one = Score.objects.order_by('-value')[0]
    # User = get_user_model()
    # user = get_object_or_404(User.objects.annotate(followers_count=Count('followers'),followings_count=Count('followings')), pk=user_pk)
    # followings = user.followings.prefetch_related(Prefetch('score_set',query_set=Score.objects.select_related('movie').order_by('value'),to_attr='score_set_value_order'))
    followings = user.followings.all()
    score_following = []
    for following in followings:
        if Score.objects.filter(user=following):
            score_following.append(Score.objects.filter(user=following).order_by('-value')[0])
    context = {'user_info':user, 'scores':scores, 'score_one':score_one, 'score_following':score_following}
    return render(request, 'accounts/detail.html', context)
    
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
@login_required    
def follow(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
        
    return redirect('accounts:detail', user_pk)