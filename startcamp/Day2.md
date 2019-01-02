# Day2

## 스크래핑 기초

### 1. 설치

```
$ pip install requests
$ pip install bs4
```

* `requests` : 요청을 대신 보내준다.
* `bs4` : 문서를 파싱하는 것을 도와준다.



requests.get('주소') : '주소'에 요청 보내서 정보를 받아줘

requests.get('주소').txt

requests.get('주소').

$ python test.py

홀짝 저장

```python
print('hello world')

# 1~100까지 저장되어 있는 것을 만들고
a = range(1,101)
# even list 를 만들어서 짝수만 저장
even = []
# odd list 를 만들어서 홀수만 저장
odd = []

for e in a:
    if (e)%2 ==0:
        even.append(e)  # even list 에 e를 추가
    else :
        odd.append(e)   # odd list 에 e를 추가
print(even)
print(odd)
```

hello world
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100][1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]



import webbrowser                                                          

webbrowser.open('https://google.com')                                      ​                                                                                                                                





파일명 앞에 이름 붙이기

