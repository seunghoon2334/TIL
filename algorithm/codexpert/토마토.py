import sys, copy
sys.stdin = open("토마토.txt")

def tomato(i,j):
    global cnt
    tomato[i][j] = 1
    if i!=0 and arr[i-1][j]==0:
        tomato(i-1,j)
    if i!=b-1 and arr[i+1][j]==0:
        tomato(i+1,j)
    if j!=0 and arr[i][j-1]==0:
        tomato(i,j-1)
    if j!=a-1 and arr[i][j+1]==0:
        tomato(i,j+1)
    cnt += 1

a, b = map(int,input().split())
arr = []
for i in range(b):
    arr.append(list(map(int, input().split())))
cnt = 0
tmp = 1
for i in range(b):
    for j in range(a):
        if arr[i][j]==1:
            tmp = 0
            tomato[i][j]
            break
    if tmp==0:
        break
print(cnt)
