import sys
sys.stdin = open("저글링 방사능 오염.txt")

def four(i,j,cnt):
    global tmp
    if arr[i-1][j]==1 and visit[i-1][j]==0:
        visit[i-1][j] = cnt+1
        tmp = 1
    if arr[i][j-1] == 1 and visit[i][j-1]==0:
        visit[i][j-1] = cnt+1
        tmp = 1
    if arr[i+1][j] == 1 and visit[i+1][j]==0:
        visit[i+1][j] = cnt+1
        tmp = 1
    if arr[i][j+1] == 1 and visit[i][j+1]==0:
        visit[i][j+1] = cnt+1
        tmp = 1

n, m = map(int,input().split()) # 가로길이 세로길이
arr = [[0 for _ in range(n+2)]]
visit = [[0 for _ in range(n+2)] for _ in range(m+2)]
for i in range(m):
    ms = input()
    s = [0]
    for ii in ms:
        s.append(int(ii))
    s.append(0)
    arr.append(s)
arr.append([0 for _ in range(n+2)])
a, b = map(int, input().split())
cnt = 1
visit[b][a] = cnt
while True:
    tmp = 0
    p = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if visit[i][j]==cnt:
                four(i,j,cnt)
                p += tmp
    if p==0:
        break
    cnt += 1

print(cnt+2)
cnt2 = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        if arr[i][j]==1 and visit[i][j]==0:
            cnt2 += 1
print(cnt2)