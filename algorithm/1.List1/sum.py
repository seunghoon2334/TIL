import sys
sys.stdin = open("sum.txt")

def mm(n, m, tt):
    min = 0
    max = 0
    for ii in range(m):#첫구간의 최소최대
        min += tt[ii]
        max += tt[ii]
    for i in range(1,n-m+1):
        mino = 0
        maxo = 0
        kk = i
        for iii in range(m):
            mino += tt[kk]
            maxo += tt[kk]
            kk += 1
        if min > mino:
            min = mino
        if max < maxo:
            max = maxo
    return (max-min)

tc = int(input())
for i in range(tc):
    t = list(map(int, input().split()))
    n = t[0]#정수의 개수
    m = t[1]#구간의 개수
    tt = list(map(int, input().split()))#숫자들
    print(f'#{i+1} {mm(n, m, tt)}')