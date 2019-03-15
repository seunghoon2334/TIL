import sys
sys.stdin = open("in.txt")

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def check(si, sj):
    dr=[-1, 1, 0, 0]
    dc=[0, 0, -1,1]
    # 4방향중 짧은 거리를 리턴
    for dep in range(1,N):# 깊이
        for k in range(4): # 4방향
            if arr[ si+dr[k]*dep ][ sj +dc[k]*dep ] ==0:
                return dep

sol=0
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            # 물의 위치에서 깊이를 계산
            sol += check(i,j)

print(sol)
