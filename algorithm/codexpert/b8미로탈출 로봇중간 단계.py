import sys
sys.stdin = open("b8미로탈출 로봇중간 단계.txt")

def up(i,j):
    global cnt, bye
    if i==0:
        return [i, j]
    while True:
        arr[i][j] = 2
        i -= 1
        if i==-1 or arr[i][j]==1:
            i += 1
            return [i, j]
        if arr[i][j]==2:
            bye = 1
            return [0,0]
        cnt += 1

def down(i,j):
    global cnt, bye
    if i==n-1:
        return [i, j]
    while True:
        arr[i][j] = 2
        i += 1
        if i==n or arr[i][j]==1:
            i -= 1
            return [i, j]
        if arr[i][j]==2:
            bye = 1
            return [0,0]
        cnt += 1

def right(i,j):
    global cnt, bye
    if j==n-1:
        return [i,j]
    while True:
        arr[i][j] = 2
        j += 1
        if j==n or arr[i][j]==1:
            j -= 1
            return [i,j]
        if arr[i][j]==2:
            bye = 1
            return [0,0]
        cnt += 1

def left(i,j):
    global cnt, bye
    if j==0:
        return [i,j]
    while True:
        arr[i][j] = 2
        j -= 1
        if j==-1 or arr[i][j]==1:
            j += 1
            return [i, j]
        if arr[i][j]==2:
            bye = 1
            return [0,0]
        cnt += 1

n = int(input())
arr = []
for _ in range(n):
    s = input()
    arr2 = []
    for j in s:
        arr2.append(int(j))
    arr.append(arr2)

i = 0
j = 0

four = list(map(int, input().split()))

bye = 0
cnt = 0
tmp = 0
while bye!=1: #1은 아래, 2는 왼쪽, 3은 위, 4는 오른쪽
    if four[tmp]==1:
        ij = down(i,j)
        i = ij[0]
        j = ij[1]
    elif four[tmp]==2:
        ij = left(i,j)
        i = ij[0]
        j = ij[1]
    elif four[tmp]==3:
        ij = up(i,j)
        i = ij[0]
        j = ij[1]
    elif four[tmp]==4:
        ij = right(i,j)
        i = ij[0]
        j = ij[1]
    tmp += 1
    if tmp==4:
        tmp -= 4
print(cnt)