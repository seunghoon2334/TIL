import sys
sys.stdin = open("in.txt")
def check(si, sj, ei, ej):
    cnt=0
    for i in range(si, ei):
        for j in range(sj, ej):
            cnt+=arr[i][j]
    return cnt

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))

cnt = [0]*4
sol=0
for i in range(1, N):
    for j in range(1, N):
        cnt[0] = check(0, 0, i, j)  # 1사분면
        cnt[1] = check(0, j, i, N)  # 2사분면
        cnt[2] = check(i, 0, N, j)  # 3분면
        cnt[3] =check(i, j, N, N)  #4분면
        if cnt[0]==cnt[1] and cnt[1]==cnt[2] and cnt[2]==cnt[3] :
            sol +=1

if sol : print(sol)
else: print(-1)

