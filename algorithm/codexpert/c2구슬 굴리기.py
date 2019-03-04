import sys
sys.stdin = open("c2구슬 굴리기.txt")

def up(i, j):
    global cnt
    while i - 1 != 0:
        i -= 1
        if arr[i][j] == 0:
            cnt += 1
        arr[i][j] = 3
        if i-1 == 0 or arr[i-1][j] == 1:
            break
    return [i, j]


def down(i, j):
    global cnt
    while i != b:
        i += 1
        if arr[i][j] == 0:
            cnt += 1
        arr[i][j] = 3
        if i == b or arr[i + 1][j] == 1:
            break
    return [i, j]


def right(i, j):
    global cnt
    while j != a:
        j += 1
        if arr[i][j] == 0:
            cnt += 1
        arr[i][j] = 3
        if j == a or arr[i][j + 1] == 1:
            break
    return [i, j]


def left(i, j):
    global cnt
    while j - 1 != 0:
        j -= 1
        if arr[i][j] == 0:
            cnt += 1
        arr[i][j] = 3
        if j - 1 == 0 or arr[i][j - 1] == 1:
            break
    return [i, j]


def go(i, j, tmp):
    if tmp == 1:
        point = up(i, j)
    elif tmp == 2:
        point = down(i, j)
    elif tmp == 3:
        point = left(i, j)
    elif tmp == 4:
        point = right(i, j)
    return point


a, b = map(int, input().split())

arr = [[0 for _ in range(a + 2)] for _ in range(b + 2)]

for i in range(1, b + 1):
    s = input()
    for j in range(a):
        arr[i][j + 1] = int(s[j])
        if int(s[j]) == 2:
            starti = i
            startj = j + 1

n = int(input())
ns = list(map(int, input().split()))
cnt = 1

i = starti
j = startj
for tmp in ns:  # 1은 위, 2는 아래, 3은 왼쪽, 4는 오른쪽
    point = go(i, j, tmp)
    i = point[0]
    j = point[1]
    # for i in range(1,b+1):
    #     print(arr[i][1:1+a])
    # print()

print(cnt)