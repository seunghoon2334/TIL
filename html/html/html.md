마우스우클릭검사(포인터 위 소스코드)또는 컨트롤쉬프트i 또는 에프12 또는 도구 더보기-개발자도구

네트워크 체크

컨트롤r

ip 

172.217.27.78

8비트(0~255)까지의 숫자로 구성된 숫자의 집합을, 각자가 가지고 있는 주소와 동일하다

도메인

네트워크상의 컴퓨터를 식별하는 호스트명

URL 

https://www/google/co.kr/search?q=구글

도메인+경로, 실제로 해당 서버(네트워크)에서 자원이 어디있는지 알려주기 위한 고유 규약

html 하이퍼텍스트마크업랭귀지

css 캐스캐이딩스타일시트

크롬스토어에서 web developer






```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

요소element

html의 element는 태그와 내용(contents)으로 구성되어 있다

self-closing element

닫는 태그가 없는 태그도 존재한다

속성Attribute

태그에는 속성이 지정될 수 있다

id class style은 태그와 상관없이 모두 사용 가능하다

DOM트리

태그는 중첩되어 사용가능하며, 이때 다음과 같은 관계를 갖는다

```html
<body>
    <h1>웹문서</h1> #body태그와 h1태그는 부모-자식 관계
    <ul>
        <li>HTML</li> #li 태그는 형제관계
        <li>CSS</li> # h1태그와 ul태그는 형제관계
    </ul>
</body>
```

시맨틱태그

컨텐츠의 의미를 설명하는 태그로서,  HTML5에 새롭게 추가된 시맨틱 태그가 있다

header-헤더(문서 전체나 섹션의 헤더)

nav-네비게이션

asode-사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용

section-문서의 일반적인 구분으로 컨텐츠의 그룹을 표현하며, 일반적으로 h1~h6 요소를 가짐

article-문서,페이지,사이트 안에서 독립적으로 구분되는 영역(포럼/신문 등의 글 또는 기사)

footer-푸터(문서 전체나 섹션의 푸터)



```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>HTML연습</title>
        <style>
            body {
                height: 10000px;
            }
            table, tr, td {
                border: 1px solid skyblue;
            }
        </style><!--구분선 주기--> <!--text-align: center;--><!--color: dasfasjdfl;-->
    </head>
    <body>
        <a href="#a">링크로 가기</a>
        <!-- 여기는 주석입니다. -->
        <h1 id="heading">heading1</h1>
        <h2>2</h2>
        <h3>3</h3>
        <h4>4</h4>
        <h5>5</h5>
        <h6>6</h6>
        <p>p태그를 사용하면 한줄 아래에서 작성가능합니다.</p>
        <p><b>Lorem ipsum</b> dolor sit amet consectetur, adipisicing elit. Numquam neque debitis consectetur officia? Quia, hic? Corporis, illum tempora nam pariatur vitae inventore vero tenetur, laboriosam eos laborum blanditiis veritatis ab?</p>
        <br> <!--엔터-->
        <hr> <!--선 쫙-->
        <p>위에 작성한 것은 <strong>Lorem Ipsum</strong>으로 임의의 문자열을 나타냅니다.</p>
        <strong>strong태그와 b태그는 모두 bold체를 표현한다.</strong>
        <em>이탤릭체도 작성가능합니다.</em>
        <i>i로도 작성 가능합니다. 다만, em이 시맨틱한 의미를 가지고 있습니다.</i>
        <p><del>취소선을 나타냅니다.</del></p> <!--글 위에 취소선 쫙-->
        <p><mark>하이라이팅</mark>도 가능합니다.</p> <!--기본 노란색-->
        <p>log<sub>10</sub>10</p>
        <p>2<sup>3</sup></p>
        <p>아&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;아</p>
        <pre> <!--문자 그대로 표현하기 위해 사용-->
            import random
            random.sample(range(1,46), 6)
            띄         어     쓰    기
        </pre>
        <q id="q">안녕하세요, 인용문입니다. 짧을 때 사용해요.</q>
        <blockquote>인용문이지만, 긴 문장입니다.
            아마도 들여쓰기가 기본적으로 적용됩니다. 
            엔터는 불가
        </blockquote>
        <ul>
            <li>순서가 없습니다.</li>
            <li style="list-style-type: square">뿡뿡이</li>
            <li>붕붕이</li>
        </ul>
        <ol>
            <li>1교시</li>
            <li>2교시</li>
            <!--li*6 후 탭-->
            <li>3교시!</li>
            <li>4교시!</li>
            <li>5교시!</li>
            <li>6교시!</li>
            <li>7교시!</li>
            <li>8교시!</li>
            <!--컨트롤+알트 누르면 여러곳 한번에 수정가능-->
        <!--reversed:거꾸로, start="":몇번부터 시작, type="a":a부터시작-->
        <ol reversed>
            <li>1교시</li>
            <li>2교시</li>
            <li>3교시</li>
            <li value="10">4교시</li> <!--여기부터 10부터-->
            <li>5교시</li>
        </ol>
        </ol>
        <!--ul>li*3 탭-->
        <!--emmet-->
        <ul>
            <li>사과</li>
            <li>바나나</li>
            <li>딸기</li>
        </ul>
        <a href="https://google.com">구글로 가기</a>
        <a href="https://google.com" target="_blank">새창으로 구글로 가기</a>
        <a href="https://google.com" target="_self">여기에서 구글로 가기</a>
        <a href="#heading">상단으로 가기</a>
        <a href="#q">인용문으로 가기</a>
        <a href="hello.html" target="_blank">hello, world!</a>
        <a href="templates/test.html">test</a>
        <a href="mailto:t@t.t">메일 보내기</a>
        <img href="https://www.google.com/" alt="GOOGLE">
        <form action="https://www.ssafy.com/">
            <input type="submit" value="ssafy">
        </form>
        <table> <!--tr*2>td*2-->
            <tr>
                <th colspan="2">표 실습</th>
            </tr>
            <tr>
                <td>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td colspan="2">1</td>>
            </tr>
            <tr> <!--tr:vvvvv,td:>>>>>-->
                <td rowspan="2">4</td>
                <td>2</td>
            </tr>
            <tr>
                <td>3</td>
            </tr><!--td scope="col" , "row" ??-->
        </table>
        <hr>
        <h2>Form input</h2>
        <form action="https://search.naver.com/search.naver" method="get">
            일반텍스트 : <input name="username" type="text" placeholder="뿡뿡이" autofocus><br>
            이메일 : <input type="email" placeholder="이메일을 입력해주세요" autocomlete="email"><br>
            비밀번호 : <input type="password" placeholder="비밀번호를 입력해주세요"><br>
            날짜 : <input type="date">
            <input type="hidden" name="hidden" value="이 사람은 누구">
            <input type="submit" value="전송"><br>
            <!--raido button-->
            <input type="radio" name="gender" value="male"> 남자
            <input type="radio" name="gender" value="female" checked> 여자<br>
            <!--checkbox-->
            <input type="checkbox" name="option"value="1">IU<br>
            <input type="checkbox" name="option"value="2">UI<br>
            <input type="checkbox" name="option"value="3">AI<br>
            <!--dropdown-->
            <select name="menu">
                <option value="korea">한식</option>
                <option value="japan" disabled>일식</option>
                <option value="china">중식</option>
                <option value="europe" selected>양식</option>
            </select>
            <input name="number" type="range" min="0" max="100" step="10">
            <a href="https://www.w3schools.com/tags/att_input_type.asp">html input type attribute</a>
            <br>ID : <input name="ID" type="text" placeholder="user"><br>
            PWD : <input type="password" placeholder="****"><input type="submit" value="로그인"><br>
        </form>
        <imag></imag>
        <imag href="C:\TIL\SSAFY\Image\my_photo.png" id="photo"></imag>
        <a href="#photo">내 사진</a>
    </body>
</html>
```

![1547454104289](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547454104289.png)

![1547454113139](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547454113139.png)

![1547454126420](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547454126420.png)

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <style>
        p {
            font-weight: bold;
        }
        </style>
    </head>
    <body>
        <form>
            <h1>FORM</h1>
            <p>주문서를 작성하여 주십시오</p><br>
            지점명 <input type="text" value="덕명점" readonly><br>
            이름 : <input type="text" placeholder="이름을 입력해주세요" required autofocus><br>
            날짜 : <input type="date" placeholder="2019. 01. 03.">

            <h2><strong>1. 샌드위치 선택</strong></h2>
            <input type="radio" name="sandwitch" checked>에그 마요<br>
            <input type="radio" name="sandwitch">이탈리안 비엠티<br>
            <input type="radio" name="sandwitch">터키 베이컨 아보카도<br>
            <hr>
            <h2>2. 사이즈 선택</h2>
            <input type="number" min="15" max="30" step="15" required>
            <hr>
            <h2>3. 빵</h2>
            <select name="bread">
                <option value="1" selected>허니오트</option>
                <option value="2" disabled>플랫브레드</option>
                <option value="3">하티 이탈리안</option>
            </select>
            <hr>
            <h2>4. 야채/소스</h2>
            <input type="checkbox" name="option" value="1">토마토<br>
            <input type="checkbox" name="option" value="2">오이<br>
            <input type="checkbox" name="option" value="3">할라피뇨<br>
            <input type="checkbox" name="option" value="4">핫 칠리<br>
            <input type="checkbox" name="option" value="5">바베큐<br>
            <input type="submit" value="submit">
        </form>

        <form action="https://google.com/search">
            <input name="q"><br>
            <input type="submit" value="구글검색">
        </form>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/aiCk8eA_nGQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/314406555&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>
    </body>
</html>
```



![1547454059489](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547454059489.png)

![1547454070925](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547454070925.png)


http://info.cern.ch/ 