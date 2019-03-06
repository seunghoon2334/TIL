import sys #586
sys.stdin = open("d1snake.txt")

n = int(input())#정사각형크기
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
k = int(input())#과일개수

for kc in range(k):
    r, c = map(int, input().split()) #가로세로
    arr[r][c] = 1
L = int(input())#뱀이동경로
xLD = []
for Lc in range(L):
    x, LD = input().split()
    xLD.append([int(x),LD])
snakelen = 1
snake = [[1,1]]
tmp = 3#right3 up2 left1 down0
r = 1
c = 1
time = 0
tt = 0
j = 0
while snakelen!=1+k or tt!=3:#경로출발
    time += 1
    if tmp==3:#진행방향에 따른 좌표 변환
        c += 1
    elif tmp==0:
        r += 1
    elif tmp==1:
        c -= 1
    elif tmp==2:
        r -= 1
    if r>n or c>n or r<1 or c<1:#벽에부딪히면
        tt = 3
        break
    elif [r, c] in snake:#자기몸에부딪히면
        tt = 3
        break
    else:
        snake.append([r, c])
        if arr[r][c] == 1:#먹이를찾으면
            arr[r][c] = 0
            snakelen += 1
        else:
            snake.pop(0)

    if time==xLD[j][0]:
        if xLD[j][1] == 'L':
            tmp -= 1
            if tmp < 0:
                tmp += 4
        elif xLD[j][1] == 'D':
            tmp += 1
            if tmp > 3:
                tmp -= 4
        j += 1

print(time)