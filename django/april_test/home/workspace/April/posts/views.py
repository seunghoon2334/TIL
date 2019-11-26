from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'posts/list.html', context)

@login_required
def create(request):
    # Q2-2, Q2-3 문제의 답안 코드를 pass를 지우고 아래에 작성하세요.
    post = Post()
    if request.method=='POST':
        if request.user.is_authenticated:
            post_form = PostForm(request.POST)
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('posts:list')
    else:
        post_form = PostForm()
        context = {'form':post_form}
        return render(request, 'posts/form.html', context)

@login_required
def like(request, post_id):
    # Q3-3 문제의 답안 코드를 pass를 지우고 아래에 작성하세요.
    post = Post.objects.get(id=post_id)
    user = request.user
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    if user in post.like_users:
        tmp = 0
    else:
        tmp = 1
    context = {'tmp':tmp}
    return redirect('posts:list', context)