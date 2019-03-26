import sys
sys.stdin = open('단지 번호붙이기.txt')

def four(i,j):
    global cnt, tmp
    visit[i][j] = cnt
    tmp += 1
    if arr[i-1][j]==1 and visit[i-1][j]==0:
        four(i-1,j)
    if arr[i][j-1] == 1 and visit[i][j-1] == 0:
        four(i, j-1)
    if arr[i+1][j] == 1 and visit[i+1][j] == 0:
        four(i+1, j)
    if arr[i][j+1] == 1 and visit[i][j+1] == 0:
        four(i, j+1)

n = int(input())
arr = [[0 for _ in range(n+2)]]
for i in range(n):
    s = input()
    arr2 = [0]
    for ii in s:
        arr2.append(int(ii))
    arr2.append(0)
    arr.append(arr2)
arr.append([0 for _ in range(n+2)])
visit = [[0 for _ in range(n+2)] for _ in range(n+2)]
cnt = 0
result = []
for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]==1 and visit[i][j]==0:
            cnt += 1
            tmp = 0
            four(i,j)
            result.append(tmp)
print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i])