import sys
import heapq
sys.stdin = open("최소 비용.txt")

def check(x,y):
    if x<0 or y<0 or x>n-1 or y>n-1:
        return False
    if visit[x][y] :
        return False
    return True

def solve(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    D[x][y] = 0
    heapq.heappush(heap,(D[x][y],x,y))

    while True:
        d,x,y = heapq.heappop(heap)

        visit[x][y] = 1
        if x==n-1 and y==n-1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx,ny):
                diff = 0
                if h[nx][ny] > h[x][y]:
                    diff = h[nx][ny] - h[x][y]
                if D[nx][ny] > (D[x][y] + diff + 1):
                    D[nx][ny] = D[x][y] + diff + 1
                    heapq.heappush(heap, (D[x][y] + diff + 1, nx, ny))

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    h = [list(map(int,input().split())) for _ in range(n)]
    D = [[99999999 for _ in range(n)] for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    heap = []
    solve(0,0)
    print('#{} {}'.format(tc,D[n-1][n-1]))