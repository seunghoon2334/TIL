import sys
sys.stdin = open("in.txt")

N = int(input())
arr = [[1]*(N+2) for _ in range(N+2)] # 가장자리1처리
for i in range(1, N+1): #1행1열부터 입력받음
    arr[i] = [1] + list(map(int, input())) + [1]

dirArr = list(map(int, input().split())) #4개의 방향
dr = [0, 1, 0, -1, 0] # 아래1, 왼2, 위3, 오른4
dc = [0, 0, -1, 0, 1]
dirNo = 0 #방향 순서
r ,c= 1,1 #현재좌표
arr[1][1]=2
cnt=0
while True:
    # 가던 진행방향으로 1칸 이동하여 좌표 계산
    r += dr[dirArr[dirNo]]
    c += dc[dirArr[dirNo]]
    # 현위치가 0이면 카운트, 방문표시
    if arr[r][c]==0:
        cnt+=1
        arr[r][c]=2
    # 현위치가 1이면 이전좌표로 재이동, 다음방향증가
    elif arr[r][c]==1:# 벽또는 장애물이면
        r -= dr[dirArr[dirNo]]
        c -= dc[dirArr[dirNo]]
        dirNo = (dirNo+1)%4 #방향전환
    # 현위치가 2이면 방문한 자리이므로   탈출
    else: break
print(cnt)



