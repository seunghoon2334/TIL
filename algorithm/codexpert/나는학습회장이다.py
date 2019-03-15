import sys
sys.stdin = open("in.txt")

N = int(input())
arr = [[0]*5 for _ in range(4)]

for i in range(1, N+1):
    score = list(map(int, input().split()))
    for j in range(3):
        arr[j+1][score[j]] += 1

for i in range(1, 4):
    for j in range(1, 4):
        arr[i][4] += arr[i][j]*j


rmax=1
flag=0
for i in range(2, 4):
    if arr[rmax][4] < arr[i][4]:
        flag=1
        rmax=i
    elif arr[rmax][4] == arr[i][4]:
        for j in range(3, 1, -1):
            #print(arr[i][j], arr[rmax][j], i, j, rmax, j)
            if arr[i][j] == arr[rmax][j] : continue
            else:
                if arr[i][j] > arr[rmax][j] : rmax=i
                flag=1
                break

if flag==0: print(0, arr[rmax][4])
else: print(rmax, arr[rmax][4])










