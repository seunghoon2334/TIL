y, x = map(int, input().split())
arr = []
for _ in range(y):
    arr.append(list(map(int, input().split())))
for i in range(y):
    cnt = 0
    for j in range(x):
        if arr[i][j] == 1:
            cnt += 1
            arr[i][j] = cnt
        else:
            cnt = 0

for i in range(y):
    result = ''
    for j in range(x):
        result += str(arr[i][j]) + ' '
    print(result)