import sys
sys.stdin = open("최소 신장 트리.txt")

t = int(input())
for tc in range(1,t+1):
    v, e = map(int,input().split())
    graph = [[9999, i] for i in range(v+1)]
    visit = [0 for _ in range(v+1)]
    es = []
    for i in range(e):
        es.append(list(map(int,input().split())))
    graph[0][0] = 0
    start = 0
    result = 0
    while True:
        visit[start] = 1
        result += graph[start][0]
        for i in range(e):
            if es[i][0] == start:
                if graph[es[i][1]][0] > es[i][2]:
                    graph[es[i][1]][0] = es[i][2]
            if es[i][1] == start:
                if graph[es[i][0]][0] > es[i][2]:
                    graph[es[i][0]][0] = es[i][2]
        p = 9999
        for i in range(v+1):
            if visit[i]==0:
                if graph[i][0] < p:
                    p = graph[i][0]
                    start = i
        if visit == [1 for _ in range(v+1)]:
            break
    print('#{} {}'.format(tc,result))