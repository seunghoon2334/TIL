import sys
sys.stdin = open("c1사냥꾼.txt")

def u(i,j):
    while arr[i-1][j]==2:
        i -= 1
        rabbit[i][j] = 1

def d(i,j):
    while arr[i+1][j]==2:
        i += 1
        rabbit[i][j] = 1

def l(i,j):
    while arr[i][j-1]==2:
        j -= 1
        rabbit[i][j] = 1

def r(i,j):
    while arr[i][j+1]==2:
        j += 1
        rabbit[i][j] = 1

def ul(i,j):
    while arr[i-1][j-1]==2:
        i -= 1
        j -= 1
        rabbit[i][j] = 1

def ur(i,j):
    while arr[i-1][j+1]==2:
        i -= 1
        j += 1
        rabbit[i][j] = 1

def dl(i,j):
    while arr[i+1][j-1]==2:
        i += 1
        j -= 1
        rabbit[i][j] = 1

def dr(i,j):
    while arr[i+1][j+1]==2:
        i += 1
        j += 1
        rabbit[i][j] = 1

def search(i,j):
    u(i,j)
    d(i,j)
    l(i,j)
    r(i,j)
    ul(i,j)
    ur(i,j)
    dl(i,j)
    dr(i,j)

n = int(input())
arr = [[0 for _ in range(n+2)] for _ in range(n+2)]
rabbit = [[0 for _ in range(n+2)] for _ in range(n+2)]
for i in range(n):
    s = input()
    for ii in range(len(s)):
        arr[i+1][ii+1] = int(s[ii])

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]==1:
            search(i,j)

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if rabbit[i][j]==1:
            cnt += 1
print(cnt)