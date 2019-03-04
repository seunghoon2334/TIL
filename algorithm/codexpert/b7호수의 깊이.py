import sys
sys.stdin = open("b7호수의 깊이.txt")

def up(i,j):
    cnt = 0
    while arr[i][j]!=0:
        i -= 1
        cnt += 1
    return cnt

def down(i,j):
    cnt = 0
    while arr[i][j] != 0:
        i += 1
        cnt += 1
    return cnt

def right(i,j):
    cnt = 0
    while arr[i][j] != 0:
        j += 1
        cnt += 1
    return cnt

def left(i,j):
    cnt = 0
    while arr[i][j] != 0:
        j -= 1
        cnt += 1
    return cnt

def four(i,j):
    result1 = up(i,j)
    result2 = down(i,j)
    result3 = right(i,j)
    result4 = left(i,j)
    return min(result1,result2,result3,result4)

n = int(input())
arr=[]
for i in range(n):
    arr2 = []
    s = input().split()
    for ii in range(len(s)):
        arr2.append(int(s[ii]))
    arr.append(arr2)
result = 0
for i in range(1,n-1):
    for j in range(1,n-1):
        result += four(i,j)
print(result)