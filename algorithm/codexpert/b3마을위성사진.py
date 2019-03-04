import sys
sys.stdin = open("b3마을위성사진.txt")

n = int(input())
arr=[[0 for _ in range(n+2)]]
for i in range(n):
    arr2 = [0]
    s = input()
    for i in s:
        arr2.append(int(i))
    arr2.append(0)
    arr.append(arr2)
arr.append([0 for _ in range(n+2)])

cnt = 1
result = 0
while cnt<100:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]>=cnt:
                if arr[i+1][j]!=0 and arr[i-1][j]!=0 and arr[i][j+1]!=0 and arr[i][j-1]!=0:
                    arr[i][j] = min(arr[i+1][j],arr[i-1][j],arr[i][j+1],arr[i][j-1]) + 1
                    if arr[i][j]>result:
                        result = arr[i][j]
    cnt += 1

if result==0:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]==1:
                result = 1
print(result)