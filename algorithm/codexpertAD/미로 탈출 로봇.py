import sys
sys.stdin = open("미로 탈출 로봇.txt")

def four(i,j,cnt):
    if arr[i-1][j]==0:
        arr[i-1][j]=cnt-1
    elif arr[i-1][j]==3:
        result.append(cnt)
        return 1
    if arr[i][j-1] == 0:
        arr[i][j-1] = cnt-1
    elif arr[i][j-1]==3:
        result.append(cnt)
        return 1
    if arr[i+1][j] == 0:
        arr[i+1][j] = cnt-1
    elif arr[i+1][j]==3:
        result.append(cnt)
        return 1
    if arr[i][j+1] == 0:
        arr[i][j+1] = cnt-1
    elif arr[i][j+1]==3:
        result.append(cnt)
        return 1
    return 0

x, y = map(int,input().split())
sx, sy, ex, ey = map(int,input().split())
arr = [[1 for _ in range(x+2)]]
for i in range(y):
    s = [1]
    ss = input()
    for ii in ss:
        s.append(int(ii))
    s.append(1)
    arr.append(s)
arr.append([1 for _ in range(x+2)])
arr[ey][ex] = 3
result = []
cnt = -1
arr[sy][sx]=-1
p=0
while True:
    for i in range(1,y+1):
        for j in range(1,x+1):
            if arr[i][j]==cnt:
                p = four(i,j,cnt)
                if p==1:
                    break
        if p == 1:
            break
    cnt -= 1
    if p == 1:
        break

print(-result[0])