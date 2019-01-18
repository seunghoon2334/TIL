import requests

for i in range(5):
    url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={837+i}"

    response = requests.get(url).json()
    lotto_numbers = []
    for ii in range(1,7):
        lotto_numbers.append(response[f"drwtNo{ii}"])
    lotto_numbers.append(response[f"bnusNo"])

    print(f'{837+i}회차 {lotto_numbers}')

