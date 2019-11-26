# 1. user1의 정보들
user1 = User.objects.get(pk=1)
user1.name
# 2. user1의 관계된 정보들
user1.post_set.all()
user1.comment_set.all()
# 3. post1(n)의 유저(1) 정보
post1 = Post.objects.get(pk=1) # Post 오브젝트
post1.user # User 오브젝트
post1.user.name # User 오브젝트의 이름
# 4. user1이 작성한 모든 댓글의 내용을 출력하는 코드
for comment in user1.comment_set.all():
    print(comment.content)
    
{% for comment in user1.comment_set.all(): %}
    {{ comment.content }}
{% endfor %}
# 5. 각각의 게시글마다 댓글을 출력
posts = Post.objects.all()
# 쿼리셋, post의 오브젝트 모두 담겨있는
for post in posts:
    for comment in post.comment_set.all():
        print(comment.content)
# detail
context = {'post':post}
{{ post.id }}번째 글
{% for comment in post.comment_set.all %}
    {{ comment.content }}
{% endfor %}

# detail -2
context = {'post':post, 'comments':post.comment_set.all() }
{% for comment in comments %}
    {{ comment.content }}
{% endfor %}
# 6. id가 2인 댓글을 쓴 사람의 게시물들은?
Post.objects.filter(user=Comment.objects.filter(id=2)[0].user)
comment = Comment.objects.get(pk=2)
comment.user.post_set.all()
Comment.objects.filter(id=2)[0].user.post_set.all()
# 7. 1번 글의 댓글들 중 첫번째 댓글을 쓴 사람의 이름은?
post1.comment_set.first().user.name
post1.comment_set.all()[0].user.name
# 8. 1번 글의 댓글 중 2,3,4을 가지고 온다면?
Post.objects.get(pk=1).comment_set.all()[1:4] # OFFSET 1 LIMIT 3
# 9. 1번 글의 두번째 댓글을 쓴 사람의 게시물들 중 첫번째인 것의 사람의 이름은?
Post.objects.get(pk=1).comment_set.all()[1].user.post_set.all()[0].user.name
# 10. 오브젝트가 아닌 특정한 컬럼의 값을 가지고 오는 경우
Comment.objects.all().values('user')
# SELECT * FROM comment
# SELECT user FROM comment

# 11. 게시물을 pk값의 내림차순으로 가지고 온다면?
Post.objects.order_by('-pk') # 내림차순 = 오름차순은 그냥

# 12. 1글 이라는 제목이 있는 게시글?
Post.objects.filter(title='1글')

# 13. 제목에 1이 들어가있는 게시글
# LIKE %%
Post.objects.filter(title__contains='1')
# Post.objects.filter(title__icontains='1')

# 14. 댓글들 중에서 해당하는 글의 제목에 1이 들어가는 경우
Comment.objects.filter(post__title__contains='1')