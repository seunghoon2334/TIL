import requests
import os
import csv

codes = []
with open('boxoffice.csv', 'r', encoding='utf-8', newline='') as f:
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
    for i in range(3):
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

with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'openDt', 
        'showTm', 'genres', 'directors', 'audits', 'actors']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in movie2.values():
        write.writerow(l)