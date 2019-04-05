import sys
sys.stdin = open("사람 네트워크2.txt")

t = int(input())
for tc in range(1,t+1):
    es = list(map(int,input().split()))
    n = es.pop(0)
    adj = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            adj[i][j] = es[cnt]
            if i != j and adj[i][j]==0:
                adj[i][j] = 99999
            cnt += 1

    for k in range(n):
        for i in range(n):
            if i==k: continue
            for j in range(i+1,n,1):
                if j==k or j==i: continue
                if adj[i][j] > adj[i][k] + adj[k][j]:
                    adj[j][i] = adj[i][k] + adj[k][j]
                    adj[i][j] = adj[i][k] + adj[k][j]
    result = 99999
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += adj[i][j]
        if tmp < result:
            result = tmp

    print('#{} {}'.format(tc,result))