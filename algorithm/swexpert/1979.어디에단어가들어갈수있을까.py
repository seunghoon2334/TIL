import sys
sys.stdin = open("1979.txt")

def search1(i,j,key):
    cnt = 1
    while j!=n-1:
        if arr[i][j+1]==1:
            visit1[i][j] = 1
            cnt += 1
            j += 1
        else:
            break
    if cnt==key:
        return 1
    else:
        return 0

def search2(i,j,key):
    cnt = 1
    while i != n - 1:
        if arr[i+1][j] == 1:
            visit2[i][j] = 1
            cnt += 1
            i += 1
        else:
            break
    if cnt == key:
        return 1
    else:
        return 0

t = int(input())
for tc in range(1,t+1):
    n, key = map(int, input().split())
    arr = []
    for i in range(n):
        arr2 = list(map(int, input().split()))
        arr.append(arr2)
    visit1 = [[0 for _ in range(n)] for _ in range(n)]
    visit2 = [[0 for _ in range(n)] for _ in range(n)]
    result = 0
    for i in range(n):#가로
        for j in range(n-key+1):
            if arr[i][j]==1 and visit1[i][j]==0:
                result += search1(i,j,key)

    for i in range(n-key+1):#세로
        for j in range(n):
            if arr[i][j]==1 and visit2[i][j]==0:
                result += search2(i,j,key)

    print('#{} {}'.format(tc,result))