import sys
sys.stdin = open("b2색종이(중).txt")

arr = [[0 for _ in range(100)] for _ in range(100)]
n =int(input())#색종이수
cnt = 0
for i in range(n):
    x, y = map(int,input().split())
    for ii in range(10):
        arr[x+ii][y:y+10] = [1 for _ in range(10)]
key = arr[0]
cnt += key.count(1)
for i in range(1,100):
    for ii in range(100):
       if arr[i][ii]!=key[ii]:
           cnt += 1
    key = arr[i]
cnt += arr[99].count(1)

for i in range(100):
    for ii in range(100):
        if i<ii:
            arr[i][ii], arr[ii][i] = arr[ii][i], arr[i][ii]

key = arr[0]
cnt += key.count(1)
for i in range(1,100):
    for ii in range(100):
       if arr[i][ii]!=key[ii]:
           cnt += 1
    key = arr[i]
cnt += arr[99].count(1)

print(cnt)