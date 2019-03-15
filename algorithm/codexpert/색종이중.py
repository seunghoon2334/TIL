
N = int(input())
arr = [[0]*102 for i in range(102)]

for k in range(N):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j]=1
cnt=0
for i in range(101):
    for j in range(101):
         if arr[i][j]==1:
             if arr[i-1][j] ==0 : cnt+=1 # 위쪽
             if arr[i +1][j] == 0: cnt += 1  # 아래쪽
             if arr[i ][j-1] == 0: cnt += 1  # 왼쪽
             if arr[i ][j +1] == 0: cnt += 1  # 오른쪽

print(cnt)