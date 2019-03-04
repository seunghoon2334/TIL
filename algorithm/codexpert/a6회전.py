n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

angle = -1
while angle != 0:
    angle = int(input())
    newarr = [[0 for _ in range(n)] for _ in range(n)]
    if angle == 90:
        for i in range(n):
            for j in range(n):
                newarr[i][j] = arr[n - 1 - j][i]
        arr = newarr
    elif angle == 180:
        for i in range(n):
            for j in range(n):
                newarr[i][j] = arr[n - 1 - i][n - 1 - j]
        arr = newarr
    elif angle == 270:
        for i in range(n):
            for j in range(n):
                newarr[i][j] = arr[j][n - 1 - i]
        arr = newarr
    elif angle == 360:
        pass
    elif angle == 0:
        break
    for i in range(n):
        s = ''
        for j in range(n):
            s += str(arr[i][j]) + ' '
        print(s)