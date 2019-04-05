import sys
sys.stdin = open("최소 이동 거리.txt")

def getMinIdx():
    minV = 999999
    minIdx = 0
    for i in range(n+1):
        if visit[i] == 0 and d[i] < minV:
            minIdx = i
            minV = d[i]
    return minIdx

def dijkstra(goal):
    d[0] = 0

    for i in range(n+1):
        if arr[0][i]:
            d[i] = arr[0][i]
    visit[0] = 1

    while True:
        node = getMinIdx()
        visit[node] = 1
        if node == goal:
            return d[goal]

        for x in range(n+1):
            if arr[node][x]:
                if d[x] > d[node] + arr[node][x]:
                    d[x] = d[node] + arr[node][x]

t = int(input())
for tc in range(1,t+1):
    n, e = map(int,input().split())
    arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    d = [99999999] * (n+1)
    for i in range(e):
        n1, n2, w = map(int,input().split())
        arr[n1][n2] = w
    print('#{} {}'.format(tc,dijkstra(n)))