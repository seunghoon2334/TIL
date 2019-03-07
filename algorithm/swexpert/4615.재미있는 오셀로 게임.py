import sys
sys.stdin = open("4615.txt")

def reverse(key):
    if key==1:
        return 2
    else:
        return 1

def cntkey(key):
    if key == 1:
        cnt[1] += 1
        cnt[2] -= 1
    else:
        cnt[2] += 1
        cnt[1] -= 1

def up(i,j,key):
    tmpi = i
    tmpj = j
    tmp = 0
    while tmpi!=0:
        tmpi -= 1
        if arr[tmpi][tmpj]==key:
            tmp = 1
            break
        if arr[tmpi][tmpj]==0:
            break
    if tmp==1:
        while i!=1:
            if arr[i-1][j]==reverse(key):
                cntkey(key)
                i -= 1
                arr[i][j]=key
            else:
                break
def upleft(i,j,key):
    tmpi = i
    tmpj = j
    tmp = 0
    while tmpi!=0 and tmpj!=0:
        tmpi -= 1
        tmpj -= 1
        if arr[tmpi][tmpj]==key:
            tmp = 1
            break
        if arr[tmpi][tmpj]==0:
            break
    if tmp == 1:
        while i!=1 or j!=1:
            if arr[i-1][j-1]==reverse(key):
                cntkey(key)
                i -= 1
                j -= 1
                arr[i][j]=key
            else:
                break
def left(i,j,key):
    tmpi = i
    tmpj = j
    tmp = 0
    while tmpj!=0:
        tmpj -= 1
        if arr[tmpi][tmpj]==key:
            tmp = 1
            break
        if arr[tmpi][tmpj]==0:
            break
    if tmp == 1:
        while j!=1:
            if arr[i][j-1]==reverse(key):
                cntkey(key)
                j -= 1
                arr[i][j]=key
            else:
                break
def downleft(i,j,key):
    tmpi = i
    tmpj = j
    tmp = 0
    while tmpi!=n+1 and tmpj!=0:
        tmpi += 1
        tmpj -= 1
        if arr[tmpi][tmpj]==key:
            tmp = 1
            break
        if arr[tmpi][tmpj]==0:
            break
    if tmp == 1:
        while i!=n or j!=1:
            if arr[i+1][j-1]==reverse(key):
                cntkey(key)
                i += 1
                j -= 1
                arr[i][j]=key
            else:
                break
def down(i,j,key):
    tmpi = i
    tmpj = j
    tmp = 0
    while tmpi!=n+1:
        tmpi += 1
        if arr[tmpi][tmpj]==key:
            tmp = 1
            break
        if arr[tmpi][tmpj]==0:
            break
    if tmp == 1:
        while i!=n:
            if arr[i+1][j]==reverse(key):
                cntkey(key)
                i += 1
                arr[i][j]=key
            else:
                break
def downright(i,j,key):
    tmpi = i
    tmpj = j
    tmp = 0
    while tmpi!=n+1 and tmpj!=n+1:
        tmpi += 1
        tmpj += 1
        if arr[tmpi][tmpj]==key:
            tmp = 1
            break
        if arr[tmpi][tmpj]==0:
            break
    if tmp == 1:
        while i!=n or j!=n:
            if arr[i+1][j+1]==reverse(key):
                cntkey(key)
                i += 1
                j += 1
                arr[i][j]=key
            else:
                break
def right(i,j,key):
    tmpi = i
    tmpj = j
    tmp = 0
    while tmpj!=n+1:
        tmpj += 1
        if arr[tmpi][tmpj]==key:
            tmp = 1
            break
        if arr[tmpi][tmpj]==0:
            break
    if tmp == 1:
        while j!=n:
            if arr[i][j+1]==reverse(key):
                cntkey(key)
                j += 1
                arr[i][j]=key
            else:
                break
def upright(i,j,key):
    tmpi = i
    tmpj = j
    tmp = 0
    while tmpi!=0 and tmpj!=n+1:
        tmpi -= 1
        tmpj += 1
        if arr[tmpi][tmpj]==key:
            tmp = 1
            break
        if arr[tmpi][tmpj]==0:
            break
    if tmp == 1:
        while i!=1 or j!=n:
            if arr[i-1][j+1]==reverse(key):
                cntkey(key)
                i -= 1
                j += 1
                arr[i][j]=key
            else:
                break

def eight(i,j,key):
    if i!=1:
        up(i,j,key)
    if i!=1 and j!=1:
        upleft(i,j,key)
    if j!=1:
        left(i,j,key)
    if j!=1 and i!=n:
        downleft(i,j,key)
    if i!=n:
        down(i,j,key)
    if i!=n and j!=n:
        downright(i,j,key)
    if j!=n:
        right(i,j,key)
    if j!=n and i!=0:
        upright(i,j,key)

t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    arr = [[0 for _ in range(n+2)] for _ in range(n+2)]
    arr[n//2][n//2] = 2
    arr[n//2+1][n//2] = 1
    arr[n//2][n//2+1] = 1
    arr[n//2+1][n//2+1] = 2
    cnt = [0,2,2]

    # for i in range(1,n+1):
    #     print(arr[i][1:n+1])

    for mm in range(m):
        i, j, key = map(int, input().split())
        arr[i][j] = key
        cnt[key] += 1
        eight(i,j,key)
    print('#{} {} {}'.format(tc,cnt[1],cnt[2]))