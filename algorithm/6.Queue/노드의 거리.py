import sys
sys.stdin = open("노드의 거리.txt")

def bfs(v):
    global arr, V
    queue = []

    queue.append(v)
    visited[v] = 1
    while len(queue)!=0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if arr[t][w]==1 and visited[w]==0:
                queue.append(w)
                visited[w] = visited[t] + 1

t = int(input())
for tc in range(t):
    V, E = map(int,input().split())
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int,input().split())
        arr[i][j] = 1
        arr[j][i] = 1
    start, end = map(int, input().split())

    bfs(start)
    if start==end:
        result = 0
    elif visited[end]==0:
        result = 0
    else:
        result = visited[end]-1
    print(f'#{tc+1} {result}')