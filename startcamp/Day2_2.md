# Day2

## 스크래핑 기초

### 1) 설치

```powershell
$ pip install requests
$ pip install bs4
```

* [requests](http://docs.python-requests.org/en/master/) : 요청을 대신 보내준다.
* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) : 문서를 파싱하는 것을 도와준다. 

### 2) 코스피 지수 가져오기

1. 네이버에서 증권 페이지를 요청한다. 
2. 페이지에서 내가 찾고 싶은 내용을 찾는다.

```python
import requests
from bs4 import BeautifulSoup

url = "https://finace.naver.com/sise"
# 1. 요청
response = requests.get(url)
# 2. 컴퓨터가 이해하는 방식으로 변환(text(string) -> html)
soup = BeautifulSoup(response.text, 'html.parser')
# 3. 원하는 정보를 CSS selector를 활용하여 가져오기
kospi = soup.select("#KOSPI_now")
# 4. 출력하기
print(kospi.text)
```



## 2. HTML/CSS 

### 1. HTML

HTML은 HyperText Markup Language의 약자로, 웹 문서에서 활용이 된다. 

웹 문서의 구조와 내용을 담당한다. 

```html
<!Doctype html>
<html>
    <head>
        <!-- 문서의 정보를 담고 있다.-->
        <title>네이버</title>
    </head>
    <body>
        <!-- 문서의 내용을 담고 있다. 실제로 브라우저에서 보이는 내용이 여기에 해당함. -->
    </body>
</html>
```

### 2. CSS

CSS는 Cascading Style Sheets의 약자로, HTML과 같은 마크업 언어를 꾸며주는 역할을 한다. 

꾸며주기 위해서 특정한 태그를 선택해야하는데 이때 활용되는 것이 `CSS 선택자(selector)`라고 부른다. 

* `id` : #
* `class` : .
* `tag`

```html
<html>
    <head>
        <style>
            #blue {
                color: blue;
            }
            .red {
                color: red;
            }
            p {
                color: skyblue;
            }
        </style>
    </head>
    <body>
        <p class="red">클래스 적용</p>
        <p id="blue">아이디 적용</p>
        <p>태그 적용</p>
        <p id="blue" class="red">파란색</p>
        <p style="color: red;">인라인 속성</p>
    </body>
</html>
```



## 3. 파일 조작

### 1.  `os` 외장 함수

```python
import os
# 1. 내가 원하는 위치로 이동 - cd
os.chdir(r'경로')
# 2. 해당 디렉토리 내에 있는 파일명 가져오기 - ls
files = os.listdir()
# 3. 파일명 바꾸기
for file in files:
    os.rename(file, "지원자"+file)
```



### 2.  file 열어서 조작하기

#### 1) 기본 사용법 

```python
with open("파일명", "w") as file:
    file.write("글써짐")
    
with open("파일명", "r") as file:
    line = file.read()
    print(line)
```

파일을 조작하는 모드는 다음과 같다. 

*  w : write(덮어쓰기)
* r : read(읽기)
* a : append(이어쓰기)

#### 2) 파일 읽기

```python
# 1. read() : 전체를 하나의 string
lines = file.read() # 전체 내용

# 2. readline() : 한줄씩 string으로 가져옴.
line = file.readline() # 첫번째 줄
line = file.readline() # 두번째 줄

# 3. readlines() : 전체를 하나의 list, element는 한 줄의 string
lines = file.readlines()
for line in lines:
    print(line.strip('\n'))
```





