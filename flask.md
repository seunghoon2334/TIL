# ORM(flask-sqlalchemy)

1. 기본 설정

   ```bash
   $ pip install flask_sqlalchemy flask_migrate
   ```

   ```python
   # app.py
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_migrate import Migrate
   
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
   db = SQLAlchemy(app)
   
   migrate = Migrate(app, db)
   
   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), unique=True, nullable=False)
       email = db.Column(db.String(120), unique=True, nullable=False)
       create_at = db.Column(db.String(80), nullable=False)
       
       def __init__(self, username, email):
           self.username = username
           self.email = email
           self.create_at = datetime.datetime.now().strftime("%D")
       
       def __repr__(self):
           return f'{self.id}: {self.username}'
   ```

2. flask db 설정

   -초기 설정(`migration` 폴더 생성)

   ```bash
   $ flask db init
   ```

   -migration 파일 생성

   ```bash
   $ flask db migrate
   ```

   -db 반영

   ```bash
   $ flask db upgrade
   ```

3. 활용법

   1.Create

   ```python
   # user 인스턴스 생성
   user = User(username='뿡뿡', email='bbung@bboong')
   # db.session.add 명령어를 통해서 추가
   # INSERT INTO user (username, email)
   # VALUES ('뿡뿡', 'bbung@bboong);
   db.session.add(user)
   # db에 반영
   db.session.commit()
   ```

   2.READ

   ```python
   # SELECT * FROM user;
   users = User.query.all()
   # get 메소드는 primary key로 지정된 값을 통해 가져온다.
   user = User.query.get(1)
   # 특정 컬럼의 값을 가진 것을 가져오려면 다음과 같이 쓴다.
   user = User.query.filter_by(username='뿡뿡').all()
   user = User.query.filter_by(username='뿡뿡').first()
   ```

   3.Update

   ```python
   user = User.query.get(1)
   user.username = '홍길동'
   db.session.commit()
   ```

   4.DELETE

   ```python
   user = User.query.get(1)
   db.session.delete(user)
   db.session.commit()
   ```

```
pip install werkzeug
```

```python
from werkzeug.security import generate_password_hash, check_password_hash

a = 'hihi'
# 암호화
hash = generate_password_hash(a)
print(hash)
# 차이점 확인
check_password_hash(hash, 'hihi')
check_password_hash('hihi', hash)
```





```
git config --global user.name ___
git config --global user.email _____
git init
git add .
git commit -m ''
git remote add origin ''
git push {-f} origin master
```

