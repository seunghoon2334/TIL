import requests
import os
import csv

images = []
code = []
with open('movie_naver.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        images.append(row['image'])
        code.append(row['movieCd'])

for i in range(len(images)):
    with open(f'images/{code[i]}.jpg', 'wb') as g:
        imaget = requests.get(images[i]).content
        g.write(imaget)