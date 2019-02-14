import sys
sys.stdin = open("그래프경로.txt")

t = int(input())
for tc in range(t):
    V, E = map(int, input().split())
    G = [[0 for i in range(V + 1)] for j in range(V + 1)]
    visited = [0 for i in range(V + 1)]
    for e in range(E):
        node1, node2 = map(int, input().split())
        G[node1][node2] = 1
    start, end = map(int, input().split())

    for i in range(len(G)):
        print(G[i])

    visit = start
    stack = [start]
    while stack[-1]!=end:
        if not 1 in G[start] and start==visit:
            result = 0
            break
        elif not 1 in G[start]:
            stack.pop(-1)
            start = stack[-1]
        else: # 1 이 G[start]에 있다면
            if G[start][end]==1:
                result = 1
                break
            else:
                point = G[start].index(1)
                stack.append(point)
                G[start][point] = 0
                start = point
        if stack==[]:
            result = 0
            break
        result = 1
    print(f'#{tc+1} {result}')