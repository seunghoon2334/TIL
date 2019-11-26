from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import Profile
from .forms import UserCustomChangeForm, UserCustomCreationForm, ProfileForm
from django.http import JsonResponse, HttpResponseBadRequest
# Create your views here.
@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('accounts:profile_update')
    else:
        user_form = UserCustomCreationForm()
    context = {'user_form': user_form}
    return render(request, 'accounts/signup.html', context)

# def signup(request):
#     return redirect('http://django-intro-thjeong2230.c9users.io:8080/posts/')
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method== 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        login_form = AuthenticationForm()
    context = {'login_form': AuthenticationForm()}
    return render(request, 'accounts/login.html', context)
    
@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:list')

@login_required
def delete(request):
    request.user.delete()
    return redirect('posts:list')
    
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        user_form = UserCustomChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('posts:list')
    else:
        user_form = UserCustomChangeForm(instance=request.user)
    context = {'user_form': user_form}
    return render(request, 'accounts/update.html', context)
    
@login_required
def password(request):
    if request.method == 'POST':
        user_form = PasswordChangeForm(request.user, request.POST) # 순서 주의!
        if user_form.is_valid():
            user = user_form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:list')
    else:
        user_form = PasswordChangeForm(request.user) # instance 아님 주의!
    context = {'user_form': user_form}
    return render(request, 'accounts/update.html', context)
    
def fake(request):
    return render(request, 'accounts/fake.html')
    
def visit(request):
    return render(request, 'accounts/visit.html')

@login_required
def profile_update(request):
    try:
        request.user.profile
    except:
        Profile.objects.create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:profile')
    profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form':profile_form}
    return render(request, 'accounts/profile_update.html', context)

@login_required    
def profile(request):
    return render(request, 'accounts/profile.html')
    
@login_required
def detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    context = {'user_info':user}
    return render(request, 'accounts/detail.html', context)

@login_required    
def follow(request, user_pk):
    if request.is_ajax():
        User = get_user_model()
        user = get_object_or_404(User, pk=user_pk)
        # if request.user in user.followers.all():
        #     user.followers.remove(request.user)
        # else:
        #     user.followers.add(request.user)
        if request.user in user.followers.all():
            user.followers.remove(request.user)
            is_follow = False
        else:
            user.followers.add(request.user)
            is_follow = True
        # return redirect('accounts:detail', user_pk)
        return JsonResponse({'is_follow':is_follow, 'followercount':user.followers.count(), 'followingcount':user.followings.count() })
    else:
        return HttpResponseBadRequest
    
def search(request):
    # 1. 내가 만들어놓은 모델
    # 2. variable routing (X)
    # 3. form (O)
    username = request.GET.get('username')
    User = get_user_model()
    user = User.objects.filter(username=username).first()
    if not user:
        return redirect('posts:list')
    return redirect('accounts:detail', user.pk)
    
def userlist(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'accounts/list.html', context)