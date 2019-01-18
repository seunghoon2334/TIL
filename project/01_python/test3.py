import requests
import os
import csv

names = []
codes = []
with open('boxoffice.csv', 'r', encoding='utf-8', newline='') as f:
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

with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'image', 'link', 'userRating']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in movie3.values():
        write.writerow(l)