# CSS(Cascading Style Sheet)



셀렉터 {프로퍼티: 값}

## 프로피터 값의 단위

1.키워드 - 단어

2.크기 - px(대부분 1px은 1/96인치, 디바이스별로 달라질수 있다), %, em, rem, viewport(vw-너비1/100,vh-높이1/100,vmin,vmax)

3.색상 - HEX(#ffffff),  RGB(rgb(0, 0, 0)), RGBA(rgb(0, 0, 0, 0.5))

## box model

### display

1. block - 항상 새로운 라인에서 시작한다.  화면 크기 전체의 가로폭을 차지한다. (width: 100%)  block 레벨 요소 내에 inline 레벨 요소를 포함할 수 있다 

   ex) div, h1 ~ h6, p, ol, ul, li, hr, table, form

2. inline - 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다.  content의 너비만큼 가로폭을 차지한다.  width, height, margin-top, margin-bottom 프로퍼티를 지정할 수 없다.  상, 하 여백은 line-height로 지정한다. 

   ex) span, a, strong, img, br, input, select, textarea, button

3. inline-block - block과 inline 레벨 요소의 특징을 모두 갖는다.  inline 레벨 요소처럼 한 줄에 표시 되면서  block에서의 width, height, margin(top, bottom) 속성을 모두 지정할 수 있다.

4. none - 해당 요소를 화면에 표시하지 않는다. (공간조차 사라진다)

### visibility Property

1. visible - 해당 요소를 보이게 한다.(기본값)
2. hidden - 해당 요소를 안보이게 한다. (공간은 존재한다.) 

### Position - 요소의 위치를 정의

1. static (기본위치) - 기본적인 요소의 배치 순서에 따라  위에서 아래로, 왼쪽에서 오른쪽으로 순서에 따라 배치되며  부모 요소 내에 자식 요소로서 존재할 때는  부모 요소의 위치를 기준으로 배치된다.
2. relative (상대위치) - 기본 위치(static으로 지정되었을 때의 위치)를 기준으로  좌표 프로퍼티(top, bottom, left, right)를 사용하여 위치를 이
3. absolute (절대위치) - 부모 요소 또는 가장 가까이 있는 조상 요소(static 제외)를 기준으로  좌표 프로퍼티(top, bottom, left, right)만큼 이동한다.   즉, relative, absolute, ﬁxed 프로퍼티가 선언되어 있는  부모 또는 조상 요소를 기준으로 위치가 결정된다.
4. fixed (고정위치) - 부모 요소와 관계없이 브라우저의 viewport를 기준으로  좌표프로퍼티(top, bottom, left, right)을 사용하여 위치를 이동시킨다.  스크롤이 되더라도 화면에서 사라지지 않고 항상 같은 곳에 위치한다.







relative : position 적용전(static일때) 자기자신이 원래 있었던 위치

​		: 움직이고 원래 있었떤 공간이 유지됨

absolute : 가장 가까운 조상 중에 static이 아닌 것의 위치

​		: 집 나감





```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        h2 {
            color: burlywood;
        }
    </style>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1 style="color: aqua">inline css 적용</h1>
    <h2>내부참조, embedding</h2>
    <h3>외부참조, 파일 link</h3>
</body>
</html>
```

```css
html {
    font-size: 20px;
}
ol, ol li {
    font-size: 1.2rem;
}
/* 주석 */
ul, ul li {
    font-size: 1.2em;
}
.vh {
    font-size: 5vh;
}
.vw {
    font-size: 5vw;
}
.vmin {
    font-size: 10vmin;
}
```

![1547540788093](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540788093.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="01.css">
</head>
<body>
    <p>20px</p>
    <ol>
        <!-- li : html*1.2 == 20*1.2-->
        <li>1.2rem</li>
    </ol>
    <ul>
        <!--ul : html*1.2-->
        <!--li : ul*1.2 == 20*1.2*1.2-->
        <li>1.2em</li>
    </ul>
    <p class="vh">5vh</p>
    <p class="vw">5vw</p>
    <p class="vmin">10vmin</p>
</body>
</html>
```

```css
/* id>class>tag>*/
* {
    color: red;
}

h1 {
    color: blue;
}

.pink {
    color: pink !important;
}/* 순서 무시 가장 중요 !important */

#yellow {
    color: yellow;
}
h2 {
    color: white;
}
.blue {
    color: blue;
}
.bold {
    font-weight: bold;
}
```

![1547540779942](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540779942.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="02.css">
</head><!--상위 경로 ../-->
<body>
    <p>빨간색</p>
    <h1>Tag 선택자</h1>
    <h2 class="pink">클래스 선택자</h2>
    <h3 id="yellow">id 선택자</h3>
    <h3 id="yellow" class="pink">yellow</h3>
    <h2 class="pink" id="yellow">id > class > tag > *</h2>
    <!-- css를 적용시키기 위해서는 마크업을 하고 선택자를 부여한다.
    span, div태그는 의미는 없지만 css 적용을 위해서 활용한다.
    -->
    <p><span class="pink">핑크색</span>, 
        <span id="yellow">노란색</span></p>
    <p class="bold blue pink">볼드체</p><!-- css 코드 상의 순서가 뒤에 있는것으로 덮어씌움-->
    <p><strong>볼드체</strong></p>
    <p><b>볼드체</b></p>
</body>
</html>
```

```css
/* 그룹 선택자 */
p, h1, h2, h3 {
    color: gray;
}
.black_bg, .white {
    color: white;
    background-color: #000000;
}
div {
    width: 100px;
    height: 100px;
    border: 1px solid black;
}
.red {
    background-color: rgba(255, 0, 0, 0.3);
}
.blue {
    background-color: rgb(0, 0, 255);
}
/* 인접 선택자 */
.red + .blue + div {
    background-color: purple;
}
/* h1 + p : h1 바로 뒤 p, h1 ~ p : h1 밑에 p */
h1 ~ p {
    color: violet;
}
h1 + p {
    color: aqua;
}
/* ol 안에 li , ol 안에 div안에 li는 x*/
ol > li {
    color: lightgreen;
}
/* ol 중에 chocolate인것 안에 li들 */
ol#chocolate > li{
    color: chocolate;
}
/* div.blue.white.pink */
/* <div class="blue white pink"> */
/* ul 안에 어디든 li */
ul li {
    color: lime;
}/* ul li~li : 2번째부터 = ul li+li */
ul li+li+li {
    color: fuchsia;
}/* 2번형제만 : ul li:nth-of-type(2)
    2번아들만 : ul li:nth-child(2)*/
ul li:nth-child(2) {
    color: royalblue;
}
```

![1547540772629](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540772629.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="03.css">
</head>
<body>
    <p>그룹 선택자 적용</p>
    <h3>그룹 선택자 적용</h3>
    <p class="black_bg">그룹</p>
    <p class="white">그룹</p>
    <hr>
    <!-- 인접 선택자 -->
    <!-- .red + .blue + div -->
    <div class="red"></div>
    <div class="blue"></div>
    <div></div>
    <hr>
    <!-- h1 + p -->
    <h1>h1</h1>
    <p>h1 p</p>
    <!-- h1 ~ p-->
    <h1>h1</h1>
    <h2>h2</h2>
    <p>h1 형제 p</p>
    <hr>
    <ol>
        <li>ol 자식 li</li>
    </ol>
    <ol id="chocolate">
        <li>허쉬</li>
        <li>드림카카오99%</li>
        <li>쿠앤크</li>
    </ol>
    <div id="chocolate">
        <li>화이트초코</li>
    </div>
    <ul>
        <div>
            <li>ul 자식 li</li>
            <li>둘째아들</li>
            <li>셋째아들</li>
        </div>
    </ul>
</body>
</html>
```

```css
.square {
    width: 100px;
    height: 100px;
    background-color: paleturquoise;
}

.padding-10 {
    padding: 10px;
}

.border-box {
    box-sizing: border-box;
}

.margin-100 {
    margin: 100px;
}

.margin-top-100 {
    margin-top: 100px;
}/* top right bottom left */

.margin-50 {
    margin: 10px 20px 30px 40px;
}

.margin-3 {
    /* top left,right bottom */
    margin: 10px 20px 30px;
}

.margin-2 {
    /* top,bottom left,right */
    margin: 10px 20px;
}

.border {
    /* border: 2px solid aqua (두꼐 스타일 색깔) */
    border-style: dashed;
    border-bottom-style: double;
    border-top-style: solid;
    border-left-style: inset;
    border-bottom-color: aqua;
}

.circle {
    width: 100px;
    height: 100px;
    border-radius: 50px;
    background-color: wheat;
}

.football {
    width: 90px;
    height: 90px;
    background-color: brown;
    border-radius: 15px 75px;
}
```

![1547540756416](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540756416.png)

![1547540762124](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540762124.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="04.css">
</head>
<body>
    <!-- 기본적으로 width는 부모의 영향을 받는다.
        div가 body의 50%이므로, p태그 영역도 50%
    -->
    <div>
        <p>100%</p>
    </div>
    <div style="width: 50%">
        <p>안녕?</p>
    </div>
    <div class="square">
        <p>컨텐츠영역 100*100</p>
    </div>
    <br>
    <div class="square padding-10">
        <p>컨텐츠영역 120*120</p>
    </div>
    <br>
    <div class="square padding-10 border-box">
        <p>100*100 (padding 포함)</p>
    </div>
    <!-- 기본적으로 남은 너비는 오른쪽으로 붙는다.
        margin-left: auto; <- 왼쪽에 남은 너비를 붙인다.(오른쪽 정렬)
        margin: auto; 오른쪽/왼쪽에 반반 나눠준다.(가운데 정렬)
    -->
    <div class="square margin-100">
        <p>100*100 margin 100</p>
    </div>
    <div class="square margin-top-100">
        <p>100*100 margin top 100</p>
    </div>
    <div class="square margin-50">
        <p>100*100 margin 50</p>
    </div>
    <div class="square margin-3">
        <p>100*100 margin 10</p>
    </div>
    <div class="square" style="margin:auto">
        <p>가운데 정렬</p>
    </div>
    <div class="square" style="margin-left:auto">
        <p>오른쪽 정렬</p>
    </div> 
    <!--div.square>p{오른쪽 정렬}-->
    <div class="square border">
        <p>border 기본 설정</p>
    </div>
    <br>
    <div class="circle">

    </div>
    <br>
    <div class="football">

    </div>
</body>
</html>
```

```css
h2 {
    display: none;
}
```

![1547540484738](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540484738.png)

![1547540492387](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540492387.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="05.css">
</head>
<body>
    <h1>block</h1>
    <p>block</p>
    <div>block</div>
    인라인 : <input type="text">
    <span>인라인</span>
    <a href="https://google.com">인라인</a>
    <h2>안녕하세요</h2>
    <h2>뿡뿡이입니다</h2>
</body>
</html>
```

```css
body {
    height: 10000px;
}

.square {
    width: 100px;
    height: 100px;
    background-color: darkgray;
    position: relative;
}

.relative-box {
    position: relative;
    background-color: navy;
    top: 10px;
    left: 10px;
}

.absolute-box {
    position: absolute;
    background-color: red;
    top: 30px;
    left: 30px;
}

.fixed {
    width: 100%;
    position: fixed;
    background-color: chocolate;
    bottom: 0;
    left: 0;
    height: 15px;
}
```

![1547540466334](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540466334.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="06.css">
</head>
<body>
    <div class="square">
        <div class="relative-box square">
        </div>
    </div>
    <br>
    <div class="square">
        <div class="absolute-box square"></div>
    </div>
    <div class="fixed">
        position 연습
    </div>
</body>
</html>
```

```css
h3 {
    color: wheat;
}
```

![1547540446400](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540446400.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>BOX</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="big-box">
    <div class="small-box" id="red"></div>
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green">
        <div class="small-box" id="purple"></div>
    </div>
    <div class="small-box" id="blue">
        <div class="small-box" id="orange"></div>
    </div>
    <div class="small-box" id="pink"></div>
    
    
  </div>
</body>
</html>
```

```css
.big-box {
    position: relative;
    margin: 100px auto 500px;
    border: 5px solid black;
    width: 500px;
    height: 500px;
  }
  
  .small-box {
    width: 100px;
    height: 100px;
  }
  
  #pink {
    background-color: pink;
    position: relative;
    top: -400px;
    left: 0;
  }
  
  #blue {
    background-color: blue;
    position: relative;
    top: -200px;
    left: 100px;
  }

  #red {
    background-color: red;
    position: relative;
    top: 400px;
    left: 400px;
  }
  
  #gold {
    background-color: gold;
    position: relative;
    top: 600px;
    left: 700px;
  }
  
  #green {
    background-color: green;
    position: relative;
    top: 0;
    left: 200px;
  }
  
  /*  심화 */
  #purple {
    background-color: purple;
    position: relative;
    top: 100px;
    left: 100px;
  }
  
  #orange {
    background-color: orange;
    position: relative;
    top: -100px;
    left: 100px;
  }
```

![1547540415639](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547540415639.png)

```html

```

```css

```

