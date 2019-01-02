v 학습해야 할 내용 • 기초 문법 • 변수 및 자료형 • 문자형
1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

```python
import keyword
print(keyword.kwlist)
```



2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (floating point rounding error) 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

   a = 0.1 * 3  b = 0.3

```python
abs(a-b) <= 1e-10

import sys
abs(a-b) <= sys.float_info.epsilon
```


3. 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \ 을 작성하세요.

```python
print("줄바꿈='\\n', 탭='\\t', \='\\\\'")
```





4. “ 안녕, 철수야 ” 를 String Interpolation을 사용하여 출력하세요.

```python
name = '철수'
print('안녕, %s야' % name)
print('안녕, {}'.format(name))
print(f'안녕, {name}야')
```





5. 다음 중 형변환시 오류가 발생하는 것은? 1) str(1)      2) int(‘30’) 3) int(5)       4) bool(‘50’)

```python
str(1) = '1'
int('30') = 30
int(5) = 5
bool('50') = True
int(‘3.5’) = ValueError: invalid literal for int() with base 10: '3.5'
```




