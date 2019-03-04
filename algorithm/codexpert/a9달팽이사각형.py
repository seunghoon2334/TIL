def right(n):
    global i, j, cnt
    for _ in range(n - 1):
        j += 1
        cnt += 1
        arr[i][j] = cnt

def down(n):
    global i, j, cnt
    for _ in range(n - 1):
        i += 1
        cnt += 1
        arr[i][j] = cnt

def left(n):
    global i, j, cnt
    for _ in range(n - 1):
        j -= 1
        cnt += 1
        arr[i][j] = cnt

def up(n):
    global i, j, cnt
    for _ in range(n - 2):
        i -= 1
        cnt += 1
        arr[i][j] = cnt

n = int(input())
m = n
global i, j, cnt
i = 0
j = 0
cnt = 1
arr = [[0 for _ in range(n)] for _ in range(n)]
if n % 2 == 0:
    for _ in range(n // 2):
        arr[i][j] = cnt
        right(m)
        down(m)
        left(m)
        up(m)
        j += 1
        m -= 2
        cnt += 1
    for i in range(n):
        result = ''
        for j in range(n):
            result += str(arr[i][j]) + ' '
        print(result)
else:
    for _ in range((n // 2) + 1):
        arr[i][j] = cnt
        right(m)
        down(m)
        left(m)
        up(m)
        j += 1
        m -= 2
        cnt += 1
    for i in range(n):
        result = ''
        for j in range(n):
            result += str(arr[i][j]) + ' '
        print(result)