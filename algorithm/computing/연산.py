import sys
sys.stdin = open("연산.txt")

def bfs(n,m):
    visit[n] = 1
    q = [n]
    while len(q) != 0:
        n = q.pop(0)
        t = [n+1,n-1,n*2,n-10]
        for i in range(4):
            if t[i]==m:
                return visit[n]
            if 0 < t[i] <= 1000000:
                if visit[t[i]]==0:
                    visit[t[i]] = visit[n] + 1
                    q.append(t[i])

t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    visit = [0 for _ in range(1000001)]
    print('#{} {}'.format(tc,bfs(n,m)))