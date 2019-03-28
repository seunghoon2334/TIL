import sys
sys.stdin = open('화물 도크.txt')

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    A = [i for i in range(n)]
    for i in range(n):
        arr[i].insert(0,arr[i][1]-arr[i][0])
    arr.sort()
    time = '000000000000000000000000'
    result = 0
    for i in range(n):
        s = arr[i][1]
        e = arr[i][2]
        if time[s:e]=='0'*(e-s):
            time = time[:s] + '1'*(e-s) + time[e:]
            result += 1
    print('#{} {}'.format(tc,result))