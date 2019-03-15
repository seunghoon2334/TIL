R, C = map(int, input().split())

arr = [[1]*(C+2) for _ in range(R+2)]
for i in range(1,R+1):
    temp = list(map(int, input()))
    for j in range(1, C+1):
        arr[i][j]=temp[j-1]
        if arr[i][j]==2:
            r = i
            c = j

N = int(input())
dirArr = list(map(int, input().split()))

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
arr[r][c]=2
cnt=1
i=0
while i<N:
    r += dr[dirArr[i]]
    c += dc[dirArr[i]]
    if arr[r][c]==1:
        r -= dr[dirArr[i]]
        c -= dc[dirArr[i]]
        i+=1
        continue
    elif arr[r][c]==0 :
        cnt+=1
        arr[r][c]=2


print(cnt)