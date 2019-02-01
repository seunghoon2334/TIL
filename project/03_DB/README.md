## 01_create_table.sql : movies 테이블 생성

```sql
CREATE TABLE movies ( -- movies 테이블 만들기
    '영화코드' INTEGER PRIMARY KEY, -- 스키마 값 지정
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' INTEGER,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
-- 출력 방식 설정
.headers on
.mode column
-- csv 데이터 가져오기
.mode csv
.import boxoffice.csv movies
-- 전체 데이터 출력하기
SELECT * FROM movies;
```

## 02_crud.sql : 영화 정보 추가/삭제/수정

```sql
INSERT INTO movies -- movies에 새로운 데이터 추가하기
VALUES (20182530,'극한직업','15세이상관람가',
'이병헌',20190123,3138467,
111,'한국','코미디'
);
-- table에서 영화코드가 20040521인 영화의 데이터를 모두 출력한다
SELECT * FROM movies WHERE 영화코드 = 20040521;
-- table에서 영화코드가 20040521인 영화의 데이터를 삭제한다
DELETE FROM movies WHERE 영화코드 = 20040521;
-- table에서 영화코드가 20185124인 영화의 데이터를 모두 출력한다
SELECT * FROM movies WHERE 영화코드 = 20185124;
-- table에서 영화코드가 20185124인 영화의 감독을 '없음'으로 변경
UPDATE movies SET 감독 = '없음' WHERE 영화코드 = 20185124;
```

## 03_select.sql : 조건에 맞는 쿼리문 작성

```sql
-- 1. 상영시간이 150분 이상인 영화이름만 출력하세요.
SELECT 영화이름 FROM movies WHERE 상영시간>=150;
-- 2. 장르가 애니메이션인 영화코드와 영화이름를 출력하세요.
SELECT 영화코드, 영화이름 FROM movies WHERE 장르='애니메이션';
-- 3. 제작국가가 덴마크이고 장르가 애니메이션인 영화이름을 출력하세요.
SELECT 영화이름 FROM movies WHERE 제작국가='덴마크' and 장르='애니메이션';
-- 4. 누적관객수가 백만이 넘고, 관람등급이 청소년관람불가인 영화이름과 누적관객수를 출력하세요.
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수>1000000 and 관람등급='청소년관람불가';
-- 5. 개봉연도가 2000년 1월 1일 ~ 2009년 12월 31일 사이인 영화를 출력하세요.
SELECT 영화이름 FROM movies WHERE 개봉연도 LIKE '200%';
-- 6. 장르를 중복 없이 출력하세요.
SELECT DISTINCT 장르 FROM movies;
-- 장르의 갯수를 확인
SELECT COUNT(DISTINCT 장르) FROM movies;
```

## 04_expression.sql : `AVG` `SUM` `MIN` `MAX` 활용

```sql
-- 1. 모든 영화의 총 누적관객수를 출력하세요.
SELECT SUM(누적관객수) FROM movies;
-- 2. 가장 많은 누적관객수인 영화이름과 누적관객수를 출력하세요.
SELECT 영화이름, MAX(누적관객수) FROM movies;
-- 3. 가장 상영시간이 짧은 영화의 장르와 상영시간을 출력하세요.
SELECT 영화이름, 장르, MIN(상영시간) FROM movies;
-- 4. 제작국가가 한국인 영화의 평균 누적관객수를 출력하세요.
SELECT AVG(누적관객수) FROM movies WHERE 제작국가='한국';
-- 5. 관람등급이 청소년관람불가인 영화의 개수를 출력하세요.
SELECT COUNT(관람등급) FROM movies WHERE 관람등급='청소년관람불가';
-- 6. 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수를 출력하세요.
SELECT COUNT(*) FROM movies WHERE 상영시간>=100 and 장르='애니메이션';
```

## 05_order.sql : 조건에 맞춰 정렬

```sql
-- 1. 누적관객수 상위 5개 영화의 모든 데이터를 출력하세요.
SELECT * FROM movies ORDER BY 누적관객수 DESC LIMIT 5;
-- 2. 장르가 애니메이션인 영화를 제작국가(오름차순), 누적관객수(내림차순)순으로 정렬하여 10개만 출력하세요.
SELECT * FROM movies ORDER BY 제작국가 ASC, 누적관객수 DESC LIMIT 10;
-- 3. 상영시간이 긴 영화를 만든 감독의 이름을 10개만 출력하세요.
SELECT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10; 
```

## pjt.sqlite3 : 결과 데이터베이스 파일



## 새롭게 학습한 것들

```sql
.help
```

```sql
SELECT DISTINCT 장를 FROM movies;
```

```sql
SELECT COUNT(*) FROM movies
WHERE 상영시간 >= 100 and 장르 = '애니메이션';
```

