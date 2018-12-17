# Day1

## 1. CLI(Command Line Interface)

명령어를 통해서 사용하는 인터페이스로, 기존의 GUI(Graphic User Interface)와는 다르게 터미널(bash/shell/cmd)을 통해서 명령을 할 수 있다.

​	사전 준비사항 : [Git bash](https://gitforwindows.org) 설치

### 1. 기본 명령어

```
$ ls
```

## 2. Python

### 0) Python Style Guide(PEP-8)

[공식문서 링크](https://www.python.org/dev/peps/pep-0008/)

### 1) string 조작

```python
# 기본 방법
print("안녕하세요")
print("저는 김승훈입니다.")
print("만나서 반갑습니다.")
#=>
print("""안녕하세요
저는 김승훈입니다.
만나서 반갑습니다.
""")
```

출력결과 :

```  
안녕하세요
저는 김승훈입니다.
만나서 반갑습니다.

안녕하세요
저는 김승훈입니다.
만나서 반갑습니다.
```

### (2) String Interpolation

1. f-string

   ```python
   name = "김승훈"
   print(f"안녕하세요, {name}입니다.")
   #=> "안녕하세요, 김승훈입니다."2.
   ```

2. [pyformat](https://pyformat.info/)

   ```python
   name = "김승훈"
   english_name = "seunghoon"
   print("안녕하세요, {}입니다. My name is {}".format(name,english_name))
   #=> "안녕하세요, 김승훈입니다. My name is seunghoon"
   print("안녕하세요, {1}입니다. My name is {0}".format(name,english_name))
   #=> "안녕하세요, seunghoon입니다. My name is 김승훈"
   print("안녕하세요, {1}입니다. My name is {1}".format(name,english_name))
   #=> "안녕하세요, seunghoon입니다. My name is seunghoon"
   ```

3. 모르면 이렇게 하자

   ```python
   name = "김승훈"
   print("안녕하세요, " + name + "입니다.")
   ```

### 2) range

`range` 는 숫자의 범위를 가지고 있는 시퀀스다.

```python
print(range(5))
#=> range(0,4)

# list 형변환
a = list(range(5))
print(a)
#=> [0,1,2,3,4]

# 반복문 활용
for i in range(3):
    print(i)
#=> 0
#=> 1
#=> 2
```

### 3) List

`list` 는 배열 또는  array라고도 불린다. 인덱스를 통해 값에 접근할 수 있다.

```python
menu = ["중국집", "초밥", "고기", "분식"]
menu[0]
#=> 중국집
```

### 4) Dictionary

`Dictionary` 는 hash(해시)라고도 불린다. `key` 와 `value` 가 짝지어져있다.

```python
phonebook = {
    "중국집": "123-525"
    "초밥": "8464-5215"
    "고기": "213-987"
    "분식": "564-2123"
}
phonebook["중국집"]
#=> "123-525"
```

## 3. [마크다운](https://www.markdownguide.org/)(Markdown)

### 1. Heading

```
# H1입니다.
## H2입니다.
### H3입니다.
#### H4입니다.
##### H5입니다.
```

# H1입니다.
## H2입니다.
### H3입니다.
#### H4입니다.
##### H5입니다.

### 2. List

```
* 순서 없는 리스트
* 순서 없는 리스트

1. 순서 있는 리스트1
2. 순서 있는 리스트2
3. 순서 있는 리스트3
```

* 순서 없는 리스트
* 순서 없는 리스트

1. 순서 있는 리스트1
2. 순서 있는 리스트2
3. 순서 있는 리스트3

### 3.  코드 작성(Code snippet)

```
​```python
print("hello, world")
​```
```
```python
print("hello, world")
```

### 4. 링크 연결

```
[구글로 가는 링크](https:/google.com)
```

[구글로 가는 링크](https:/google.com)

### 5. 글씨 꾸미기

```
_기울임_
*기울임*
**굵게**
__굵게__
**_굵게기울임_**
```

*기울임*

**굵게**

**_굵게기울임_**

### 6. 기타

```
---
***
> 안녕하세요?
인용문 공간입니다.
```

---
***
> 안녕하세요?
인용문 공간입니다.





random.choice(리스트)

리스트에서 임의적으로 하나의 요소를 선택

```
import random

menu = [ ]

food = rand
```

random.sample(리스트,갯수)

리스트에서 특정 수의 요소를 임의적으로 비복원추출







append() 삽입



얼굴인식 api

autodraw.com

siraj raval - youtube

python gta v self driving

ls : list 나열
cd ___  : ___디렉토리(폴더)로 가기 change
touch ___ : ___ 만들기
mkdir : 새로운 디렉토리 생성 make
rm : 지우기  remove (폴더는 -rf)
mv _a_ _b_  :  _a_를 _b_로 바꾸기
pwd : 현재 워킹 디렉토리

git

분산형 버전 관리 시스템(DVCS :Distributed Version Control System)

코드의 history를 관리하는 도구

add 커밋할 목록에 추가

commit 커밋(create a snapshot) 만들기

push 현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기

```

$ git config --global --unset credential.help
$ git config --system --unset credential.help
나의  GitHub 계정 이메일과 본인의 영문이름으로 계정 정보 등록
$ git config --global user.name "내 이름"
$ git config --global user.email "내 이메일"
$ git config --global --list
```







```python
# 1. random 외장 함수 가져오기
import random
# 2. 1~45까지 숫자 numbers에 저장하기
numbers = range(1,46)
# 3. numbers에서 6개 뽑기
num = random.sample(numbers,6)
# 4. 출력하기
print(num)
#print(random.sample(numbers,6))
numa = num.sort()
print(type(numa))
print(num)
numb = sorted(num)
print(type(numb))
print(num)
```

```
[38, 23, 12, 9, 13, 27]
<class 'NoneType'>
[9, 12, 13, 23, 27, 38]
<class 'list'>
[9, 12, 13, 23, 27, 38]
```