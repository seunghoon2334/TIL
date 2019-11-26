## app.py

```python
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask 및 sqlalchemy 설정
app = Flask(__name__)
app.secret_key = 'fsdaaaaaaaaaaaaaaaaaaaa' # method='POST'를 쓰려면 secret_key가 필요
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 및 migration 초기화
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True) # id
    title = db.Column(db.String, unique=True, nullable=False) # 영화명
    title_en = db.Column(db.String, nullable=False) # 영화명(영문)
    audience = db.Column(db.Integer, nullable=False) # 누적관객수
    open_date = db.Column(db.String, nullable=False) # 개봉일
    genre = db.Column(db.String, nullable=False) # 장르
    watch_grade = db.Column(db.String, nullable=False) #관람등급
    score = db.Column(db.Float, nullable=False) # 평점
    poster_url = db.Column(db.TEXT, nullable=False) # 포스터 이미지 URL
    description = db.Column(db.TEXT, nullable=False) # 영화소개
    
    def __init__(self, title, title_en, audience, open_date, genre, watch_grade, score, poster_url, description): # Movie 클래스로 만들어서 값을 저장
        self.title = title
        self.title_en = title_en
        self.audience = audience
        self.open_date = open_date
        self.genre = genre
        self.watch_grade = watch_grade
        self.score = score
        self.poster_url = poster_url
        self.description = description
        
    def __repr__(self):
        return f'{self.title}: {self.score}'

@app.route('/movies/') # 기본 페이지
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
    
@app.route('/movies/new') # 새로 등록
def new():
    return render_template('new.html')

@app.route('/movies/create', methods=['POST'])
def create(): #요청 받아서 만들기
    # title = request.form.get('title')
    # title_en = request.form.get('title_en')
    # audience = request.form.get('audience')
    # open_date = request.form.get('open_date')
    # genre = request.form.get('genre')
    # watch_grade = request.form.get('watch_grade')
    # score = request.form.get('score')
    # poster_url = request.form.get('poster_url')
    # description = request.form.get('description')
    # movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    movie = Movie(**request.form)
    db.session.add(movie)
    db.session.commit()
    return redirect('/movies/')
    
@app.route('/movies/<int:id>') 
def show(id): # 상세보기
    movie = Movie.query.get(id)
    return render_template('show.html', movie=movie)
    
@app.route('/movies/<int:id>/edit/')
def edit(id): # 수정하기
    movie = Movie.query.get(id)
    return render_template('edit.html', movie=movie)

@app.route('/movies/<int:id>/update/', methods=['POST'])
def update(id): # 수정 내용 받아서 변경
    movie = Movie.query.get(id)
    # movie.title = request.form.get('title')
    # movie.title_en = request.form.get('title_en')
    # movie.audience = request.form.get('audience')
    # movie.open_date = request.form.get('open_date')
    # movie.genre = request.form.get('genre')
    # movie.watch_grade = request.form.get('watch_grade')
    # movie.score = request.form.get('score')
    # movie.poster_url = request.form.get('poster_url')
    # movie.description = request.form.get('description')
    
    for key, value in dict(request.form).items():
        movie.key = value
    # for key, value in request.form.items():
    #     setattr(movie, key, value)    
    db.session.commit()
    flash(f'영화 정보 수정이 완료되었습니다.', 'success')
    return redirect('/movies/')

@app.route('/movies/<int:id>/delete/')
def delete(id): # 내용 삭제
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/movies/')

if __name__ == '__main__': # 기본 주소
    app.run(host='0.0.0.0', port='8080', debug=True)
```

## index.html

```html
{% extends 'base.html' %} 
{% block body %}
    <h1>영화 목록</h1>
    <a href='/movies/new'>새 영화 등록</a><br><br>
    {% for movie in movies %}
        <a href='/movies/{{movie.id}}'>{{movie.title}}</a><p> : {{movie.score}} </p>
        <hr>
    {% endfor %}
{% endblock %}
```

## edit.html

```html
{% extends 'base.html' %}

{% block title %}
영화수정 폼
{% endblock %}

{% block body %}
    <form action='/movies/{{movie.id}}/update/', method='POST'>
        title : <input type='text' name='title', value='{{movie.title}}'> <br>
        title_en : <input type='text' name='title_en', value='{{movie.title_en}}'> <br>
        audience : <input type='number' name='audience', value='{{movie.audience}}'> <br>
        open_date : <input type='date' name='open_date', value='{{movie.open_date}}'> <br>
        genre : <input type='text' name='genre', value='{{movie.genre}}'> <br>
        watch_grade : <input type='text' name='watch_grade', value='{{movie.watch_grade}}'> <br>
        score : <input type='number' name='score', value='{{movie.score}}', min='0', max='10', step='0.01'> <br>
        poster_url : <input type='text' name='poster_url', value='{{movie.poster_url}}'> <br>
        description : <input type="textarea" name="description", value='{{movie.description}}'>> <br>
        <input type='submit' value='수정'>
    </form>
{% endblock %}
```

## new.html

```html
{% extends 'base.html' %}

{% block title %}
영화등록 폼
{% endblock %}

{% block body %}
    <form action='/movies/create', method='POST'>
        title : <input type='text' name='title'> <br>
        title_en : <input type='text' name='title_en'> <br>
        audience : <input type='number' name='audience'> <br>
        open_date : <input type='date' name='open_date'> <br>
        genre : <input type='text' name='genre'> <br>
        watch_grade : <input type='text' name='watch_grade'> <br>
        score : <input type='number' name='score', min='0', max='10', step='0.01'> <br>
        poster_url : <input type='text' name='poster_url'> <br>
        description : <input type="textarea" name="description"> <br>
        <input type='submit' value='영화등록'>
    </form>
{% endblock %}
```

## show.html

```html
{% extends 'base.html' %}

{% block title %}
영화수정 폼
{% endblock %}

{% block body %}
    <p>*영화명  :  {{movie.title}}</p>
    <p>*영화명(영문)  :  {{movie.title_en}}</p>
    <p>*누적 관객수  :  {{movie.audience}}</p>
    <p>*개봉일  :  {{movie.open_date}}</p>
    <p>*장르  :  {{movie.genre}}</p>
    <p>*관람등급  :  {{movie.watch_grade}}</p>
    <p>*평점  :  {{movie.score}}</p>
    <img src='{{movie.poster_url}}' width="35%" height="35%"> 
    <br><br>
    <p>*영화소개  :  {{movie.description}}</p>
    
    
    <a href='/movies/'>목록 </a>
    <a href='/movies/{{movie.id}}/edit/'>수정 </a>
    <a href='/movies/{{movie.id}}/delete/'>삭제</a>
    <hr>
{% endblock %}
```

## base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %} {% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>
<body>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
            <div class="alert alert-{{category}}" role="alert">
                {{message}}
            </div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    <nav class='navbar navbar-expand-lg navbar-light bg-light'><a class="navbar-brand" href="#">영화</a></nav>
    <div class="container mt-5">
        {% block body %}
        {% endblock %}
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>
</html>
```







