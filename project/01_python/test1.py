import requests
import os
import csv

days = [20190113, 20190106, 20181230, 20181223, 20181216, 20181209, 20181202, 20181125, 20181118, 20181111]

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
    url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0&itemPerPage=10'

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

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'audiAcc', 'day']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in movie1.values():
        write.writerow(l)