import sys
sys.stdin = open("1860.txt")

t = int(input())
for tc in range(1,t+1):
    n, m ,k = map(int, input().split()) #손님수 붕어빵시간 붕어빵개수
    ns = list(map(int, input().split())) #손님오는시간
    ns.sort()
    fish = 0
    time = 0
    start = 0
    end = len(ns)
    while True:
        time += 1
        if time % m==0:
            fish += k
        if ns[0]<m:
            print('#{} Impossible'.format(tc))
            break
        if fish>=n:
            print('#{} Possible'.format(tc))
            break
        if time==ns[start]:
            fish -= ns.count(ns[start])
            start += ns.count(ns[start])
        if fish<0:
            print('#{} Impossible'.format(tc))
            break
        elif start==end:
            print('#{} Possible'.format(tc))
            break