import csv
lunch1 = {
    '맘스터치':'싸이버거',
    '노은각':'짬짜면',
    '신전떡볶이':'김밥'
}
lunch2 = [
    {
    'store':'맘스터치',
    'menu':'싸이버거'
    },
    {
    'store':'노은각',
    'menu':'짬짜면'
    },
    {
    'store':'신전떡볶이',
    'menu':'김밥'
    }
]

with open('lunch3.csv', 'w', encoding='utf-8', newline='') as f:
    write = csv.writer(f)
    write.writerow(('가게','메뉴'))
    for item in lunch1.items():
        write.writerow(item)

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for key, value in lunch1.items():
        f.write(f'{key}, {value}\n')

with open('lunch2.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['store', 'menu']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    #write.writerow({'menu': '짬짜면', 'store':'노은각'})
    for l in lunch2:
        write.writerow(l)

with open('lunch3.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['가게'], row['메뉴'])