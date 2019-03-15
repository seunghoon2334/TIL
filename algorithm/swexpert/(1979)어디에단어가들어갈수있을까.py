import sys
sys.stdin = open("(1979)어디에단어가들어갈수있을까_input.txt")
T = int(input())
MAXN = 15

for tc in range(1, T+1):
    data = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
    N, K = map(int, input().split())

    for i in range(N):
        data[i] = list(map(int, input().split()))

    ans = 0
    visit = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
    for i in range(N):  #가로
        for j in range(N):  #0:벽, 1:길
            if data[i][j] == 0  or visit[i][j] == 1: continue
            cnt = 0
            while j < N and data[i][j] == 1:
                visit[i][j] = 1
                cnt += 1
                j += 1
            if cnt == K : ans += 1

    visit = [[0 for _ in range(MAXN)] for _ in range(MAXN)] #다시 초기화
    for i in range(N):  #가로
        for j in range(N):
            if data[j][i] == 0 or visit[j][i] == 1: continue
            cnt = 0
            while j < N and data[j][i] == 1:
                visit[j][i] = 1
                cnt += 1
                j += 1
            if cnt == K : ans += 1

    print("#{} {}".format(tc, ans))