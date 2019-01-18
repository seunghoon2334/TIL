



# git bash

`vi ~/.bash_profile` 입력

i(nsert)를 누르고

`export kobis_key="dddddddd"`

`export naver_secret="dddddd"`

`export naver_id="ddddddddd"`

`esc`

`:wq`를 입력해서 탈출

`source ~/.bash_profile`입력



여기서 등록한 키를 받을때는

```:ballot_box_with_check:
import os
key = os.getenv('kobis_key)
```



```python
import requests #url로 요청을 보내서 값을 가져온다.
import csv #파일을 저장 또는 불러오기시 사용한다.
```

# test1.py

```python
import requests
import os
import csv

days = [20190113, 20190106, 20181230, 20181223, 20181216, 20181209, 20181202, 20181125, 20181118, 20181111] #최근 10주 날짜

movie1 = {
    } 
for tt in range(len(days)):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    key =  os.getenv('kobis_key')
    targetDt = days[tt]
    movieCd = [] #영화 대표코드
    movieNm = [] #영화제목
    audiAcc = [] #누적관객
    day = []
    url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0&itemPerPage=10' #요청변수에 추가하여 url을 추출

    response = requests.get(url).json()
    result = response['boxOfficeResult']['weeklyBoxOfficeList']

    for i in range(10):
        movieNm.append((result[i]['movieNm']))
        movieCd.append((result[i]['movieCd']))
        audiAcc.append((result[i]['audiAcc']))
        day.append((response['boxOfficeResult']['yearWeekTime']))

    for i in range(10):
        if not movieCd[i] in movie1:
            movie1.update({
                movieCd[i]:
                {'movieCd': movieCd[i], 'movieNm': movieNm[i], 'audiAcc': audiAcc[i], 'day': targetDt}
            })

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:#movie1의 내용들을 boxoffice.csv로 저장
    fieldnames = ['movieCd', 'movieNm', 'audiAcc', 'day']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in movie1.values():
        write.writerow(l)
```
###  boxoffice.csv

```
movieCd,movieNm,audiAcc,day
20184105,말모이,1185368,20190113
20176251,내안의 그놈,765383,20190113
20189463,주먹왕 랄프 2: 인터넷 속으로,1342315,20190113
20180290,아쿠아맨,4920735,20190113
20183915,극장판 공룡메카드: 타이니소어의 섬,289873,20190113
20185485,보헤미안 랩소디,9785643,20190113
20184574,그린 북,99569,20190113
20186281,범블비,1553491,20190113
20170658,PMC: 더 벙커,1665204,20190113
20175547,스윙키즈,1462874,20190113
20183785,점박이 한반도의 공룡2 : 새로운 낙원,521053,20190106
20184187,언니,172340,20190106
20182421,그린치,543815,20190106
20168773,마약왕,1787838,20181230
20183479,극장판 짱구는 못말려: 아뵤! 쿵후 보이즈 ~라면 대란~,259753,20181230
20183238,스파이더맨: 뉴 유니버스,628327,20181230
20177552,국가부도의 날,3723915,20181223
20179230,도어락,1546002,20181223
20183375,극장판 포켓몬스터 모두의 이야기,86997,20181223
20189843,호두까기 인형과 4개의 왕국,408425,20181216
20182082,부탁 하나만 들어줘,87501,20181216
20178825,모털 엔진,262070,20181216
20183745,런닝맨 : 풀룰루의 역습,180709,20181216
20177538,완벽한 타인,5270621,20181216
20184481,성난황소,1567264,20181209
20181905,후드,276658,20181209
20176814,신비한 동물들과 그린델왈드의 범죄,2403686,20181209
20183073,베일리 어게인,78439,20181202
20181171,바울,229837,20181202
20183007,거미줄에 걸린 소녀,25172,20181202
20182966,투 프렌즈,20419,20181202
20183050,번 더 스테이지: 더 무비,298402,20181125
20182935,출국,71407,20181125
20182669,툴리,24325,20181125
20186822,너의 췌장을 먹고 싶어,48910,20181125
20170513,동네사람들,445625,20181118
20189869,해피 투게더,15745,20181118
20174981,창궐,1588443,20181111
20010291,해리포터와 마법사의 돌,259733,20181111
20179006,여곡성,55997,20181111
20181404,벽 속에 숨은 마법시계,211233,20181111
20180523,스타 이즈 본,458917,20181111
20182693,구스범스: 몬스터의 역습,21400,20181111
```

# test2.py

```python
import requests
import os
import csv

codes = [] 
with open('boxoffice.csv', 'r', encoding='utf-8', newline='') as f: #boxoffice.csv에서 영화코드를 호출
    reader = csv.DictReader(f)
    for row in reader:
        codes.append(row['movieCd'])

movie2 = {
        }
for ttt in range(len(codes)):
    
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    key =  os.getenv('kobis_key')

    movieNm = [] #영화제목
    movieNmEn = [] #영화제목영문
    movieNmOg = [] #영화제목원문
    openDt = [] #개봉연도
    showTm = [] #상영시간
    genres = [] #장르
    directors = [] #감독명
    audits = [] #관람등급
    actors = []
    movieCd = codes[ttt]
    url = f'{base_url}?key={key}&movieCd={movieCd}'
    response = requests.get(url).json()
    result = response['movieInfoResult']['movieInfo']
    movieNm.append((result['movieNm']))
    movieNmEn.append((result['movieNmEn']))
    movieNmOg.append((result['movieNmOg']))
    openDt.append((result['openDt']))
    showTm.append((result['showTm']))
    genres.append((result['genres'][0].values()))
    directors.append((result['directors'][0].values()))
    audits.append((result['audits'][0].values()))
    for i in range(3): #배우가 없거나 한두명 있는 경우를 해결 가능
        if result['actors']==[]:
            break
        elif i==len(result['actors']):
            break
        else:
            actors.append((result['actors'][i].values()))

    movie2.update({
        codes[ttt]:
            {'movieCd': movieCd, 'movieNm': movieNm, 'movieNmEn': movieNmEn, 'movieNmOg': movieNmOg, 'openDt': openDt, 
            'showTm': showTm, 'genres': genres, 'directors': directors, 'audits': audits, 'actors': actors}
        })

with open('movie.csv', 'w', encoding='utf-8', newline='') as f: # movie2의 내용들을 movie.csv로 저장
    fieldnames = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'openDt', 
        'showTm', 'genres', 'directors', 'audits', 'actors']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in movie2.values():
        write.writerow(l)
```
### movie.csv

```
movieCd,movieNm,movieNmEn,movieNmOg,openDt,showTm,genres,directors,audits,actors
20184105,['말모이'],['MAL·MO·E: The Secret Mission'],[''],['20190109'],['135'],[dict_values(['드라마'])],"[dict_values(['엄유나', 'EOM Yuna'])]","[dict_values(['2018-MF02396', '12세이상관람가'])]","[dict_values(['유해진', 'YOO Hae-jin', '', '']), dict_values(['윤계상', 'YOON Kye-sang', '', '']), dict_values(['김홍파', 'KIM Hong-pa', '', ''])]"
20176251,['내안의 그놈'],['Inside me'],[''],['20190109'],['122'],[dict_values(['판타지'])],"[dict_values(['강효진', 'KANG Hyo-jin'])]","[dict_values(['2018-MF01859', '15세이상관람가'])]","[dict_values(['박성웅', 'PARK Sung-woong', '판수', '']), dict_values(['진영', '', '동현', '']), dict_values(['라미란', 'RA Mi-ran', '미선', ''])]"
20189463,['주먹왕 랄프 2: 인터넷 속으로'],['Ralph Breaks the Internet'],[''],['20190103'],['112'],[dict_values(['애니메이션'])],"[dict_values(['리치 무어', 'Rich Moore'])]","[dict_values(['2018-MF02246', '전체관람가'])]","[dict_values(['존 C. 라일리', 'John C. Reilly', '', '']), dict_values(['사라 실버맨', 'Sarah Silverman', '', '']), dict_values(['맨디 무어', 'Mandy Moore', '', ''])]"
20180290,['아쿠아맨'],['AQUAMAN'],[''],['20181219'],['143'],[dict_values(['액션'])],"[dict_values(['제임스 완', 'James Wan'])]","[dict_values(['2018-MF02303 ', '12세이상관람가'])]","[dict_values(['제이슨 모모아', 'Jason Momoa', '', '']), dict_values(['앰버 허드', 'Amber Heard', '', '']), dict_values(['니콜 키드먼', 'Nicole Kidman', '', ''])]"
20183915,['극장판 공룡메카드: 타이니소어의 섬'],[''],[''],['20190110'],['70'],[dict_values(['애니메이션'])],"[dict_values(['최신규', 'CHOE Shin-gyu'])]","[dict_values(['2018-MF02159', '전체관람가'])]",[]
20185485,['보헤미안 랩소디'],['Bohemian Rhapsody'],[''],['20181031'],['134'],[dict_values(['드라마'])],"[dict_values(['브라이언 싱어', 'Bryan Singer'])]","[dict_values(['2018-MF01972', '12세이상관람가'])]","[dict_values(['레미 맬렉', 'Rami Malek', '', '']), dict_values(['조셉 마젤로', 'Joseph Mazzello', '', '']), dict_values(['마이크 마이어스', 'Mike Myers', '', ''])]"
20184574,['그린 북'],['Green Book'],[''],['20190109'],['130'],[dict_values(['드라마'])],"[dict_values(['피터 패럴리', 'Peter Farrelly'])]","[dict_values(['2018-MF02280', '12세이상관람가'])]","[dict_values(['비고 모텐슨', 'Viggo Mortensen', '', '']), dict_values(['마허샬라 알리', 'Mahershala Ali', '', ''])]"
20186281,['범블비'],['Bumblebee'],[''],['20181225'],['113'],[dict_values(['액션'])],"[dict_values(['트래비스 나이트', 'Travis Knight'])]","[dict_values(['2018-MF02395', '12세이상관람가'])]","[dict_values(['헤일리 스테인펠드', 'Hailee Steinfeld', '', '']), dict_values(['파멜라 애들론', 'Pamela Adlon', '', '']), dict_values(['존 시나', 'John Cena', '', ''])]"
20170658,['PMC: 더 벙커'],['Take Point'],[''],['20181226'],['124'],[dict_values(['액션'])],"[dict_values(['김병우', 'KIM Byung-woo'])]","[dict_values(['2018-MF02410', '15세이상관람가'])]","[dict_values(['하정우', 'HA Jung-woo', '', '']), dict_values(['이선균', 'LEE Sun-kyun', '', '']), dict_values(['제니퍼 엘', 'Jennifer Ehle', '', ''])]"
20175547,['스윙키즈'],['Swing Kids'],[''],['20181219'],['133'],[dict_values(['드라마'])],"[dict_values(['강형철', 'KANG Hyoung-chul'])]","[dict_values(['2018-MF02244', '12세이상관람가'])]","[dict_values(['도경수', 'DOH Kyung-soo', '', '']), dict_values(['박혜수', '', '', '']), dict_values(['자레드 그라임스', 'Jared Grimes', '', ''])]"
20183785,['점박이 한반도의 공룡2 : 새로운 낙원'],[''],[''],['20181225'],['93'],[dict_values(['애니메이션'])],"[dict_values(['한상호', ''])]","[dict_values(['2018-MF02240', '전체관람가'])]","[dict_values(['박희순', 'PARK Hee-soon', '점박이 목소리', '']), dict_values(['라미란', 'RA Mi-ran', '송곳니 목소리', '']), dict_values(['김성균', 'KIM Sung-kyun', '싸이 목소리', ''])]"
20184187,['언니'],['No Mercy'],[''],['20190101'],['93'],[dict_values(['액션'])],"[dict_values(['임경택', 'LIM Kyoung-tack'])]","[dict_values(['2018-MF02432', '청소년관람불가'])]","[dict_values(['이시영', 'LEE Si-young', '', '']), dict_values(['박세완', 'PARK Se-wan', '', '']), dict_values(['이준혁', 'LEE Jun-hyuk', '', ''])]"
20182421,['그린치'],['The Grinch'],[''],['20181219'],['89'],[dict_values(['애니메이션'])],"[dict_values(['스콧 모시어', 'Scott Mosier'])]","[dict_values(['2018-MF02028', '전체관람가'])]","[dict_values(['베네딕트 컴버배치', 'Benedict Cumberbatch', '', ''])]"
20168773,['마약왕'],['The Drug King'],[''],['20181219'],['139'],[dict_values(['범죄'])],"[dict_values(['우민호', 'WOO Min-ho'])]","[dict_values(['2018-MF01606', '청소년관람불가'])]","[dict_values(['송강호', 'SONG Kang-ho', '이두삼', '']), dict_values(['조정석', 'JO Jung-suk', '김인구', '']), dict_values(['배두나', 'BAE Doo-na', '김정아', ''])]"
20183479,['극장판 짱구는 못말려: 아뵤! 쿵후 보이즈 ~라면 대란~'],['Crayon Shin-chan: Burst Serving! Kung Fu Boys - Ramen Rebellion'],[''],['20181219'],['103'],[dict_values(['애니메이션'])],"[dict_values(['타카하시 와타루', 'Wataru Takahashi'])]","[dict_values(['2018-MF02346', '전체관람가'])]","[dict_values(['박영남', 'PARK Yoeng-nam', '짱구 (한국어 목소리)', '']), dict_values(['강희선', 'GANG Hui-seon', '엄마/맹구 (한국어 목소리)', '']), dict_values(['김환진', 'KIM Hwan-chin', '아빠 (한국어 목소리)', ''])]"
20183238,['스파이더맨: 뉴 유니버스'],['Spider-Man: Into the Spider-Verse'],[''],['20181212'],['116'],[dict_values(['애니메이션'])],"[dict_values(['밥 퍼시케티', 'Bob Persichetti'])]","[dict_values(['2018-MF02316', '12세이상관람가'])]","[dict_values(['샤메익 무어', 'Shameik Moore', '마일스 모랄레스', '']), dict_values(['헤일리 스테인펠드', 'Hailee Steinfeld', '스파이더 그웬', '']), dict_values(['니콜라스 케이지', 'Nicolas Cage ', '스파이더맨 누아르', ''])]"
20177552,['국가부도의 날'],['Default'],[''],['20181128'],['114'],[dict_values(['드라마'])],"[dict_values(['최국희', 'CHOI Kook-hee'])]","[dict_values(['2018-MF01973', '12세이상관람가'])]","[dict_values(['김혜수', 'KIM Hye-soo', '', '']), dict_values(['유아인', 'YOO Ah-in', '', '']), dict_values(['허준호', 'HUH Joon-ho', '', ''])]"
20179230,['도어락'],['Door Lock'],[''],['20181205'],['101'],[dict_values(['스릴러'])],"[dict_values(['이권', 'LEE Kwon'])]","[dict_values(['2018-MF02157', '15세이상관람가'])]","[dict_values(['공효진', 'KONG Hyo-jin', '조경민', '']), dict_values(['김예원', 'KIM Ye-won', '오효주', '']), dict_values(['김성오', 'KIM Sung-oh', '이형사', ''])]"
20183375,['극장판 포켓몬스터 모두의 이야기'],['Pokemon the Movie: The Power of Us'],['劇場版ポケットモンスター みんなの物語'],['20181219'],['98'],[dict_values(['애니메이션'])],"[dict_values(['야지마 테츠오', 'Tetsuo Yajima'])]","[dict_values(['2018-MF02168', '전체관람가'])]",[]
20189843,['호두까기 인형과 4개의 왕국'],['The Nutcracker and the Four Realms'],[''],['20181206'],['99'],[dict_values(['판타지'])],"[dict_values(['라세 할스트롬', 'Lasse Hallstrom'])]","[dict_values(['2018-MF02136', '전체관람가'])]","[dict_values(['키이라 나이틀리', 'Keira Knightley', '', '']), dict_values(['매켄지 포이', 'Mackenzie Foy', '', '']), dict_values(['헬렌 미렌', 'Helen Mirren', '', ''])]"
20182082,['부탁 하나만 들어줘'],['A Simple Favor'],[''],['20181212'],['116'],[dict_values(['스릴러'])],"[dict_values(['폴 페이그', 'Paul Feig'])]","[dict_values(['2018-MF02209', '청소년관람불가'])]","[dict_values(['블레이크 라이블리', 'Blake Lively', '', '']), dict_values(['안나 켄드릭', 'Anna Kendrick', '', '']), dict_values(['헨리 골딩', 'Henry Golding', '', ''])]"
20178825,['모털 엔진'],['Mortal Engines'],[''],['20181205'],['128'],[dict_values(['액션'])],"[dict_values(['크리스찬 리버스', 'Christian Rivers'])]","[dict_values(['2018-MF02210', '12세이상관람가'])]","[dict_values(['헤라 힐마', 'Hera Hilmar', '헤스터 쇼', '']), dict_values(['로버트 시한', 'Robert Sheehan', '톰 내츠워디', '']), dict_values(['휴고 위빙', 'Hugo Weaving', '테데우스 발렌타인', ''])]"
20183745,['런닝맨 : 풀룰루의 역습'],['Running Man'],[''],['20181205'],['66'],[dict_values(['애니메이션'])],"[dict_values(['윤준상', 'YOON Jun-sang'])]","[dict_values(['2018-MF02189', '전체관람가'])]","[dict_values(['김서영', 'KIM Seo-young', '리우 목소리', '']), dict_values(['권창욱', '', '쿠가 목소리', '']), dict_values(['엄상현', 'UM Sang-hyun', '롱키 목소리', ''])]"
20177538,['완벽한 타인'],['Intimate Strangers'],[''],['20181031'],['115'],[dict_values(['드라마'])],"[dict_values(['이재규', 'LEE Jae-kyoo'])]","[dict_values(['2018-MF01726', '15세이상관람가'])]","[dict_values(['유해진', 'YOO Hae-jin', '', '']), dict_values(['조진웅', 'CHO Jin-woong', '', '']), dict_values(['이서진', 'LEE Seo-jin', '준모', ''])]"
20184481,['성난황소'],['Unstoppable'],[''],['20181122'],['115'],[dict_values(['범죄'])],"[dict_values(['김민호', 'KIM Min-ho'])]","[dict_values(['2018-MF02083', '15세이상관람가'])]","[dict_values(['마동석', 'Don LEE', '', '']), dict_values(['송지효', 'SONG Ji-hyo', '', '']), dict_values(['김성오', 'KIM Sung-oh', '', ''])]"
20181905,['후드'],['Robin Hood'],[''],['20181128'],['116'],[dict_values(['어드벤처'])],"[dict_values(['오토 바서스트', 'Otto Bathurst'])]","[dict_values(['2018-MF02043', '12세이상관람가'])]","[dict_values(['태런 에저튼', 'Taron Egerton', '', '']), dict_values(['제이미 폭스', 'Jamie Foxx', '', '']), dict_values(['벤 멘델슨', 'Ben Mendelsohn', '', ''])]"
20176814,['신비한 동물들과 그린델왈드의 범죄'],['Fantastic Beasts: The Crimes of Grindelwald'],['FANTASTIC BEASTS THE CRIMES OF GRINDELWALD'],['20181114'],['133'],[dict_values(['판타지'])],"[dict_values(['데이빗 예이츠', 'David Yates'])]","[dict_values(['2018-MF02044', '12세이상관람가'])]","[dict_values(['에디 레드메인', 'Eddie Redmayne', '', '']), dict_values(['캐서린 워터스턴', 'Katherine Waterston', '', '']), dict_values(['앨리슨 수돌', 'Alison Sudol', '', ''])]"
20183073,['베일리 어게인'],"[""A Dog's Purpose""]",[''],['20181122'],['100'],[dict_values(['어드벤처'])],"[dict_values(['라세 할스트롬', 'Lasse Hallstrom'])]","[dict_values(['2018-MF02082', '전체관람가'])]","[dict_values(['조시 게드', 'Josh Gad', '', '']), dict_values(['데니스 퀘이드', 'Dennis Quaid', '', '']), dict_values(['브릿 로버트슨', 'Britt Robertson', '', ''])]"
20181171,['바울'],"['Paul, Apostle Of Christ']",[''],['20181031'],['107'],[dict_values(['드라마'])],"[dict_values(['앤드류 하얏트', 'Andrew Hyatt'])]","[dict_values(['2018-MF01804', '15세이상관람가'])]","[dict_values(['제임스 폴크너', 'James Faulkner', '', '']), dict_values(['제임스 카비젤', 'James Caviezel', '', ''])]"
20183007,['거미줄에 걸린 소녀'],['THE GIRL IN THE SPIDER’S WEB'],[''],['20181128'],['115'],[dict_values(['액션'])],"[dict_values(['페드 알바레즈', 'Fede Alvarez'])]","[dict_values(['2018-MF02211', '15세이상관람가'])]","[dict_values(['클레어 포이', 'Claire Foy', '', '']), dict_values(['실비아 획스', 'Sylvia Hoeks', '', '']), dict_values(['스베리르 구드나손', 'Sverrir Gudnason', '', ''])]"
20182966,['투 프렌즈'],['TWO TAILS'],[''],['20181129'],['74'],[dict_values(['애니메이션'])],"[dict_values(['빅터 아즈에프', 'Victor Azeev'])]","[dict_values(['2018-MF02080', '전체관람가'])]",[]
20183050,['번 더 스테이지: 더 무비'],['Burn the Stage: the Movie'],[''],['20181115'],['82'],[dict_values(['기타'])],"[dict_values(['박준수', ''])]","[dict_values(['2018-MF02135', '전체관람가'])]","[dict_values(['김남준', 'RM', '', '']), dict_values(['김석진', 'JIN', '', '']), dict_values(['민윤기', 'SUGA', '', ''])]"
20182935,['출국'],['Unfinished'],[''],['20181114'],['104'],[dict_values(['드라마'])],"[dict_values(['노규엽', ''])]","[dict_values(['2018-MF01929', '15세이상관람가'])]","[dict_values(['이범수', 'LEE Beom-su', '', '']), dict_values(['연우진', 'YEON Woo-jin', '', '']), dict_values(['박혁권', 'PARK Hyuk-kwon', '', ''])]"
20182669,['툴리'],['TULLY'],[''],['20181122'],['95'],[dict_values(['드라마'])],"[dict_values(['제이슨 라이트맨', 'Jason Reitman'])]","[dict_values(['2018-MF01816', '15세이상관람가'])]","[dict_values(['샤를리즈 테론', 'Charlize Theron', '', '']), dict_values(['맥켄지 데이비스', 'Mackenzie Davis', '', '']), dict_values(['마크 듀플라스', 'Mark Duplass', '', ''])]"
20186822,['너의 췌장을 먹고 싶어'],['I want to eat your pancreas'],['君の膵臓をたべたい'],['20181115'],['109'],[dict_values(['애니메이션'])],"[dict_values(['우시지마 신이치로', 'Shinichiro Ushijima'])]","[dict_values(['2018-MF02041', '12세이상관람가'])]","[dict_values(['타카스기 마히로', 'Mahiro Takasugi', '나 (목소리)', '']), dict_values(['린', 'Lynn', '사쿠라 (목소리)', '']), dict_values(['후지이 유키요', 'Yukiyo Fujii', '쿄코 (목소리)', ''])]"
20170513,['동네사람들'],[''],[''],['20181107'],['99'],[dict_values(['액션'])],"[dict_values(['임진순', 'LIM Jin-sun'])]","[dict_values(['2018-MF01975', '15세이상관람가'])]","[dict_values(['마동석', 'Don LEE', '역기철', '']), dict_values(['김새론', 'KIM Sae-ron', '강유진', '']), dict_values(['이상엽', 'LEE Sang-yeob', '지성', ''])]"
20189869,['해피 투게더'],['Happy Together'],[''],['20181115'],['110'],[dict_values(['드라마'])],"[dict_values(['김정환', ''])]","[dict_values(['2018-MF02101', '12세이상관람가'])]","[dict_values(['박성웅', 'PARK Sung-woong', '', '']), dict_values(['송새벽', 'SONG Sae-byeok', '', '']), dict_values(['최로운', '', '', ''])]"
20174981,['창궐'],['Rampant'],[''],['20181025'],['121'],[dict_values(['사극'])],"[dict_values(['김성훈', 'KIM Sung-hoon'])]","[dict_values(['2018-MF01721', '15세이상관람가'])]","[dict_values(['현빈', 'HYUN Bin', '', '']), dict_values(['장동건', 'JANG Dong-gun', '', '']), dict_values(['조우진', 'JO Woo-jin', '', ''])]"
20010291,['해리포터와 마법사의 돌'],['Harry Potter And The Socrerers Stone'],[''],['20011213'],['152'],[dict_values(['가족'])],"[dict_values(['크리스 콜럼버스', 'Chris Columbus'])]","[dict_values(['2001-F336', '전체관람가'])]","[dict_values(['다니엘 래드클리프', 'Daniel Radcliffe', '', '']), dict_values(['엠마 왓슨', 'Emma Watson', '', '']), dict_values(['루퍼트 그린트', 'Rupert Grint', '', ''])]"
20179006,['여곡성'],['The Wrath'],[''],['20181108'],['94'],[dict_values(['공포(호러)'])],"[dict_values(['유영선', 'YOO Young-sun'])]","[dict_values(['2018-MF01703', '15세이상관람가'])]","[dict_values(['홍예리', 'HONG Yae-ree', '비류', '']), dict_values(['서영희', 'SEO Young-hee', '신씨부인', '']), dict_values(['손나은', 'SON Na-eun', '옥분', ''])]"
20181404,['벽 속에 숨은 마법시계'],['The house with a clock in its walls'],[''],['20181031'],['105'],[dict_values(['판타지'])],"[dict_values(['일라이 로스', 'Eli Roth'])]","[dict_values(['2018-MF01769', '전체관람가'])]","[dict_values(['잭 블랙', 'Jack Black', '', '']), dict_values(['케이트 블란쳇', 'Cate Blanchett', '', '']), dict_values(['오웬 바카로', 'Owen Vaccaro', '', ''])]"
20180523,['스타 이즈 본'],['A Star Is Born'],[''],['20181009'],['135'],[dict_values(['드라마'])],"[dict_values(['브래들리 쿠퍼', 'Bradley Cooper'])]","[dict_values(['2018-MF01588', '15세이상관람가'])]","[dict_values(['브래들리 쿠퍼', 'Bradley Cooper', '', '']), dict_values(['레이디 가가', 'Lady Gaga', '', '']), dict_values(['샘 엘리엇', 'Sam Elliott', '', ''])]"
20182693,['구스범스: 몬스터의 역습'],['Goosebumps 2: Haunted Halloween'],[''],['20181107'],['89'],[dict_values(['판타지'])],"[dict_values(['아리 산델', 'Ari Sandel'])]","[dict_values(['2018-MF02084', '12세이상관람가'])]","[dict_values(['잭 블랙', 'Jack Black', '', '']), dict_values(['켄 정', 'Ken Jeong', '', ''])]"

```

# test3.py

```python
import requests
import os
import csv

names = []
codes = []
with open('boxoffice.csv', 'r', encoding='utf-8', newline='') as f: # boxoffice.csv에서 영화제목과 코드를 호출
    reader = csv.DictReader(f)
    for row in reader:
        names.append(row['movieNm'])
        codes.append(row['movieCd'])
movie3 = {

}

for ttt in range(len(names)):
    base_url = 'https://openapi.naver.com/v1/search/movie.json'
    client_id = os.getenv('naver_id')
    client_secret = os.getenv('naver_secret')
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    url = f'{base_url}?query={names[ttt]}'
    response = requests.get(url, headers=headers).json()
    result = response['items'][0]

    movieCd = codes[ttt]#영화코드
    image = result['image']#썸네일이미지url
    link = result['link']#하이퍼텍스트link
    userRating = result['userRating']#유저평점

    movie3.update({
        names[ttt]:
            {'movieCd': movieCd, 'image': image, 'link': link, 'userRating': userRating}
    })

with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f: # movie3의 내용들을 movie_naver.csv로 저장
    fieldnames = ['movieCd', 'image', 'link', 'userRating']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in movie3.values():
        write.writerow(l)
```
### movie_naver.csv

```
movieCd,image,link,userRating
20184105,https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167699_P40_175859.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=167699,9.04
20176251,https://ssl.pstatic.net/imgmovie/mdi/mit110/1641/164172_P26_152224.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=164172,8.77
20189463,https://ssl.pstatic.net/imgmovie/mdi/mit110/1526/152632_P19_104759.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=152632,8.76
20180290,https://ssl.pstatic.net/imgmovie/mdi/mit110/1511/151153_P19_095147.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=151153,8.38
20183915,https://ssl.pstatic.net/imgmovie/mdi/mit110/1803/180372_P16_101254.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=180372,9.19
20185485,https://ssl.pstatic.net/imgmovie/mdi/mit110/1564/156464_P49_182103.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=156464,9.47
20184574,https://ssl.pstatic.net/imgmovie/mdi/mit110/1715/171539_P26_135622.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539,9.66
20186281,https://ssl.pstatic.net/imgmovie/mdi/mit110/1641/164139_P12_153521.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=164139,8.18
20170658,https://ssl.pstatic.net/imgmovie/mdi/mit110/1660/166092_P35_104446.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=166092,5.33
20175547,https://ssl.pstatic.net/imgmovie/mdi/mit110/1641/164101_P62_155759.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=164101,8.49
20183785,https://ssl.pstatic.net/imgmovie/mdi/mit110/1803/180379_P32_111508.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=180379,9.18
20184187,https://ssl.pstatic.net/imgmovie/mdi/mit110/1523/152344_P75_112734.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=152344,5.96
20182421,https://ssl.pstatic.net/imgmovie/mdi/mit110/1506/150688_P30_101919.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=150688,8.36
20168773,https://ssl.pstatic.net/imgmovie/mdi/mit110/1572/157297_P23_134212.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=157297,6.52
20183479,https://ssl.pstatic.net/imgmovie/mdi/mit110/1729/172975_P10_141815.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=172975,8.46
20183238,https://ssl.pstatic.net/imgmovie/mdi/mit110/1717/171725_P18_175530.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=171725,9.26
20177552,https://ssl.pstatic.net/imgmovie/mdi/mit110/1641/164192_P45_134107.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=164192,8.18
20179230,https://ssl.pstatic.net/imgmovie/mdi/mit110/1717/171755_P39_140011.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=171755,6.28
20183375,https://ssl.pstatic.net/imgmovie/mdi/mit110/1721/172187_P19_110125.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=172187,9.04
20189843,https://ssl.pstatic.net/imgmovie/mdi/mit110/1586/158622_P18_142307.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=158622,7.39
20182082,https://ssl.pstatic.net/imgmovie/mdi/mit110/1714/171452_P19_174244.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=171452,7.87
20178825,https://ssl.pstatic.net/imgmovie/mdi/mit110/1564/156496_P24_153246.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=156496,6.39
20183745,https://ssl.pstatic.net/imgmovie/mdi/mit110/1803/180384_P14_152246.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=180384,7.75
20177538,https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167638_P71_133542.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=167638,8.66
20184481,https://ssl.pstatic.net/imgmovie/mdi/mit110/1748/174835_P26_105639.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=174835,7.60
20181905,https://ssl.pstatic.net/imgmovie/mdi/mit110/1442/144266_P15_111933.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=144266,7.16
20176814,https://ssl.pstatic.net/imgmovie/mdi/mit110/1542/154255_P24_095824.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=154255,6.29
20183073,https://ssl.pstatic.net/imgmovie/mdi/mit110/1449/144906_P15_103017.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=144906,9.53
20181171,https://ssl.pstatic.net/imgmovie/mdi/mit110/1736/173692_P12_102159.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=173692,9.17
20183007,https://ssl.pstatic.net/imgmovie/mdi/mit110/1618/161868_P24_151256.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=161868,8.55
20182966,https://ssl.pstatic.net/imgmovie/mdi/mit110/1791/179138_P01_151818.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=179138,4.52
20183050,https://ssl.pstatic.net/imgmovie/mdi/mit110/1763/176354_P13_150227.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=176354,9.36
20182935,https://ssl.pstatic.net/imgmovie/mdi/mit110/1791/179139_P14_100455.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=179139,8.79
20182669,https://ssl.pstatic.net/imgmovie/mdi/mit110/1546/154653_P12_102646.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=154653,8.80
20186822,https://ssl.pstatic.net/imgmovie/mdi/mit110/1753/175318_P15_105507.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=175318,8.31
20170513,https://ssl.pstatic.net/imgmovie/mdi/mit110/1666/166610_P58_154049.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=166610,5.52
20189869,https://ssl.pstatic.net/imgmovie/mdi/mit110/1641/164147_P46_165808.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=164147,7.70
20174981,https://ssl.pstatic.net/imgmovie/mdi/mit110/1604/160487_P48_113750.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=160487,5.13
20010291,https://ssl.pstatic.net/imgmovie/mdi/mit110/0306/30688_P28_142632.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=30688,9.23
20179006,https://ssl.pstatic.net/imgmovie/mdi/mit110/1717/171750_P05_173050.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=171750,4.31
20181404,https://ssl.pstatic.net/imgmovie/mdi/mit110/1641/164155_P03_122329.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=164155,6.15
20180523,https://ssl.pstatic.net/imgmovie/mdi/mit110/1680/168050_P19_100458.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=168050,9.15
20182693,https://ssl.pstatic.net/imgmovie/mdi/mit110/1728/172819_P01_163303.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=172819,7.50
```

# test4.py


```python
import requests
import os
import csv

images = []
code = []
with open('movie_naver.csv', 'r', encoding='utf-8', newline='') as f: #movie_naver.csv에서 imageurl과 영화코드 호출
    reader = csv.DictReader(f)
    for row in reader:
        images.append(row['image'])
        code.append(row['movieCd'])

for i in range(len(images)): #image를 불러와서 image폴더에 저장
    with open(f'images/{code[i]}.jpg', 'wb') as g:
        imaget = requests.get(images[i]).content
        g.write(imaget)
```
### images/

![1547799746060](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547799746060.png)