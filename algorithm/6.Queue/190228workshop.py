import sys
sys.stdin = open("190228workshop.txt")

for tc in range(1,11):
    n, start = map(int, input().split())
    num = list(map(int,input().split()))
    arr = [[0 for _ in range(101)] for _ in range(101)]
    for i in range(0,n,2):
        arr[num[i]][num[i+1]] = 1
    visited = [0]*101
    visited[start] = 1
    finish = [start]
    cnt = 2
    while True:
        tmp = len(finish)
        for i in range(len(finish)):
            for ii in range(1,101):
                if arr[finish[i]][ii]==1 and visited[ii]==0:
                    arr[finish[i]][ii] = 0
                    finish.append(ii)
                    visited[ii] = cnt
        for i in range(tmp):
            finish.pop(0)
        if finish == []:
            break
        cnt += 1

    result = 0
    point = 0
    for i in range(101):
        if visited[i]>=point:
            point = visited[i]
            result = i
    print(f'#{tc} {result}')