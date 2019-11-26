from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q 
from .models import Post, Image, Comment, Hashtag
from .forms import PostForm, ImageForm, CommentForm
from django.http import JsonResponse

# Create your views here.
@login_required
def list(request):
    # images = Image.objects.all()
    posts = Post.objects.filter(Q(user__in=request.user.followings.values('id')) | Q(user=request.user.id)).order_by('-pk')
    context = {'posts': posts}
    # context = {'images':images}
    
# {% for image in images %}
#     <img src="{{ image.file.url }}" class="card-img-top" alt="...">
# {% endfor %}
    return render(request, 'posts/list.html', context)

@login_required    
def make(request):
    if request.method=='POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            files = request.FILES.getlist('file')
            for file in files:
                request.FILES['file'] = file
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            # 1. 내용을 공백 단위로 쪼개서 반복문을 돌리면
            for word in post.content.split():
            # 1-1. #이 가장 앞에 있으면,
                if word.startswith('#'):
            # 1-1-1. 해시태크에 저장이 되어 있으면, 가져와서 추가
            # 1-1-2. 저장이 안되어 있으면, 만들어서 추가
                    hashtag, is_created = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(hashtag)
                    # 만들어지면 : (hashtag object, True)
                    # 가져와지면 : (hashtag object, False)
            
            return redirect(post)
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {'post_form' : post_form, 'image_form': image_form}
    return render(request, 'posts/make.html', context)
    
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comments = post.comment_set.all()
    hashtags = post.hashtags.all()
    context = {'post': post, 'comments':comments, 'hashtags':hashtags, 'comment_form': CommentForm()}
    return render(request, 'posts/detail.html', context)

@login_required
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect('posts:list')
    
@login_required
def edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.save()
            post.hashtags.clear()
            for word in post.content.split():
                if word.startsweith('#'):
                    hashtag, is_created = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(hashtag)
            return redirect(post)
    else:
        post_form = PostForm(instance=post)
    context = {'post':post, 'post_form':post_form}
    return render(request, 'posts/make.html', context)
    
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        data = {'username': comment.user.username, 
                'content': comment.content,
                'postPk': comment.post.pk,
                'commentPk': comment.pk
                }
        return JsonResponse(data)
    
def comments_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('posts:detail', post_pk)
    
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    User = get_user_model()
    user = request.user
    user = user
    # user가 지금 해당 게시글에 좋아요를 한적이 있는지?
    # if user in post.liked_users.all():
    #     post.liked_users.remove(user)
    # else:
    #     post.liked_users.add(user)
    if post.liked_users.filter(pk=user.id).exists():
        post.liked_users.remove(user)
        is_like = False
    else:
        post.liked_users.add(user)
        is_like = True
    # return redirect('posts:detail', post_pk)
    return JsonResponse({'is_like': is_like, 'count': post.liked_users.count()})
    
def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    posts = hashtag.posts.all()
    context = {'posts':posts, 'hashtag':hashtag}
    return render(request, 'posts/hashtag.html', context)