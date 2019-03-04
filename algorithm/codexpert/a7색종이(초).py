arr = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for nc in range(n):
    a, b = map(int, input().split())
    for i in range(a,a+10):
        arr[i][b:b+10] = [1 for _ in range(10)]
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]==1:
            cnt += 1
print(cnt)