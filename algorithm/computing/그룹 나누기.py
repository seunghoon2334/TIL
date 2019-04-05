import sys
sys.stdin = open("그룹 나누기.txt")

t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    ms = list(map(int,input().split()))
    visit = [0 for _ in range(n+1)]
    cnt = 1
    chk = 0
    for i in range(m):
        a = visit[ms[i*2]]
        b = visit[ms[i*2+1]]
        if a==0 and b==0:
            visit[ms[i*2]] = cnt
            visit[ms[i*2+1]] = cnt
            cnt += 1
            chk += 1
        elif a==0 and b!=0:
            visit[ms[i*2]] = b
        elif a!=0 and b==0:
            visit[ms[i*2+1]] = a
        elif a!=0 and b!=0 and a!=b:
            for ii in range(1,n+1):
                if visit[ii]==b:
                    visit[ii] = a
            chk -= 1
    tmp = visit.count(0) - 1
    print('#{} {}'.format(tc, chk + tmp))