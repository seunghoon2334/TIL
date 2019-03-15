import sys
sys.stdin = open("in.txt")
def check(r, c):#현재 위치에서 8방향의 토끼 카운트
    dr=[-1, 1, 0, 0, -1, 1, -1, 1] #상하좌우,좌상,좌하,우상,우하 8방향 행의 증감치
    dc=[0, 0, -1, 1, -1, -1, 1, 1]
    cnt =0
    for k in range(8): #8방향
        for dep in range(1, N): # 현위치에서 떨어진 거리
            nr = r + dr[k]*dep
            nc = c + dc[k]*dep
            # 범위를 벗어났거나 0 또는 1 이면 탈출
            if nr<0 or nr>=N or nc<0 or nc>=N or arr[nr][nc]<2:
                break
            elif arr[nr][nc]==2: #토끼라면 지우고 카운트
                arr[nr][nc]=3
                cnt+=1
    return cnt

N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int, input())))
sol=0
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:# 사냥꾼위치에서 탐색 시작
            sol+=check(i, j)

print(sol)
