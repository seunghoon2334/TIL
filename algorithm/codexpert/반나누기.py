import sys
sys.stdin = open("in.txt")

def check(s, e):
    cnt=0
    # for i in range(s, e+1):
    #     cnt+=arr[i]
    cnt = sum(arr[s:e+1])
    if kmin <= cnt <= kmax: return cnt
    else: return 0

T = int(input())
for ti in range(T):
    N, kmin, kmax = map(int,input().split())
    arr = [0]*101
    temp = list(map(int, input().split()))
    for score in temp:
        arr[score]+=1

    T1, T2=0, 0
    sol = 1000
    cnt = [0]*3
    for i in range(1, 100-1):
        for j in range(i+1, 100):
            cnt[0] = check(1, i)
            cnt[1] = check(i+1, j)
            cnt[2] = check(j+1, 100)
            if cnt[0]*cnt[1]*cnt[2] == 0: continue
            temp = max(cnt) - min(cnt)
            if  temp < sol : sol = temp
    if sol == 1000: print(-1)
    else : print(sol)







