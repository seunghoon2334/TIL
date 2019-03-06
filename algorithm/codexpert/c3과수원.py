import sys
sys.stdin = open("c3과수원.txt")

n = int(input())
arr = []
for i in range(n):
    s = input()
    arr2 = []
    for ii in s:
        arr2.append(int(ii))
    arr.append(arr2)

cnt = 0
for i in range(1,n):
    for j in range(1,n):
        tmp1 = 0
        tmp2 = 0
        tmp3 = 0
        tmp4 = 0
        for t1 in range(0,i):
            for t2 in range(0,j):
                if arr[t1][t2]==1:
                    tmp1 += 1
        for t1 in range(0,i):
            for t2 in range(j,n):
                if arr[t1][t2]==1:
                    tmp2 += 1
        for t1 in range(i,n):
            for t2 in range(0,j):
                if arr[t1][t2]==1:
                    tmp3 += 1
        for t1 in range(i,n):
            for t2 in range(j,n):
                if arr[t1][t2]==1:
                    tmp4 += 1
        if tmp1==tmp2 and tmp2==tmp3 and tmp3==tmp4:
            cnt += 1

if cnt==0:
    result = -1
else:
    result=cnt
print(result)