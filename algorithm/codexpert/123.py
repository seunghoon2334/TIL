import sys
sys.stdin = open("123.txt")

for tc in range(1,11):
    n = int(input())  # 원본암호문길이
    string = list(input().split())  # 원본암호문
    IDAnum = int(input())  # 명령어개수
    IDA = list(input().split())  # 명령어

    for i in range(len(IDA)):
        key = IDA[i]
        if key == 'I':
            for ii in range(int(IDA[i+2])):
                string.insert(int(IDA[i+1])+ii, IDA[i+3+ii])
        elif key == 'D':
            for ii in range(int(IDA[i+2])):
                string.pop(int(IDA[i+1]))
        elif key == 'A':
            for ii in range(int(IDA[i+1])):
                string.append(IDA[i+2+ii])
    result = ''
    for i in string[0:10]:
        result += i + ' '
    print(f'#{tc} {result}')
