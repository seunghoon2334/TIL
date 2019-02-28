def bfs(v):
    global G, V
    visited = [0] * (V+1)
    queue = []
    queue.append(v)
    while len(queue)!=0:
        v = queue.pop(0)
        if not visited[v]:
            visited[v]= 1
            print(v, end=" ")
            for w in range(1, V+1):
                if G[v][w]==1 and visited[w]==0:
                    queue.append(w)


V, E = map(int, input().split())

