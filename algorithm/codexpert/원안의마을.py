import sys
sys.stdin = open("in.txt")

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
    for j in range(N):
        if arr[i][j]==2:
            sr=i
            sc=j

d, R=0,0
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            d = (sr - i)*(sr - i) + (sc-j)*(sc-j)
            if d>R: R=d

for i in range(N):
    if i*i>=R: break

print(i)