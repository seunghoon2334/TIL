import sys
sys.stdin = open("d7도넛츠 합계.txt")

def don(i, j, k):
    if k==1:
        return arr[i][j]
    elif k<=0:
        return 0
    else:
        result = 0
        for ii in range(i,i+k):
            for jj in range(j,j+k):
                result += arr[ii][jj]
        return result

n, d = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
tmp = 0
result = 0
for i in range(n-d+1):
    for j in range(n-d+1):
        tmp = don(i,j,d) - don(i+1,j+1,d-2)
        if tmp>result:
            result = tmp
print(result)