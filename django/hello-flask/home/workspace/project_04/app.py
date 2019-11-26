from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask 및 sqlalchemy 설정
app = Flask(__name__)
app.secret_key = 'fsdaaaaaaaaaaaaaaaaaaaa'
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
    
    def __init__(self, title, title_en, audience, open_date, genre, watch_grade, score, poster_url, description):
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

@app.route('/movies/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
    
@app.route('/movies/new')
def new():
    return render_template('new.html')

@app.route('/movies/create', methods=['POST'])
def create():
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
def show(id):
    movie = Movie.query.get(id)
    return render_template('show.html', movie=movie)
    
@app.route('/movies/<int:id>/edit/')
def edit(id):
    movie = Movie.query.get(id)
    return render_template('edit.html', movie=movie)

@app.route('/movies/<int:id>/update/', methods=['POST'])
def update(id):
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
    for key, value in request.form.items():
        setattr(movie, key, value)
    db.session.commit()
    flash(f'영화 정보 수정이 완료되었습니다.', 'success')
    return redirect('/movies/')

@app.route('/movies/<int:id>/delete/')
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/movies/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)