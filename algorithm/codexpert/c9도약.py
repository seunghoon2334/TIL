import sys
sys.stdin = open("c9도약.txt")
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
cnt = 0
for i in range(n - 2):
    for ii in range(i + 1, n - 1):
        for iii in range(ii + 1, n):
            if (arr[ii] - arr[i]) <= (arr[iii] - arr[ii]):
                if  (arr[iii] - arr[ii]) <= (arr[ii] - arr[i]) * 2:
                    cnt += 1
                else:
                    break
                # print(arr[i],arr[ii],arr[iii])
print(cnt)