import sys
sys.stdin = open("d2창고다각형.txt")

n = int(input())#기둥수
arr = [0 for _ in range(1002)]
LH = []
for nc in range(n):
    L, H = map(int, input().split())
    LH.append([L,H])
    arr[L] = H
result = 0
LH.sort()
startH = LH[0][1]
startL = LH[0][0]
height = startH
maxh = max(arr)

for i in range(LH[0][0],LH[n-1][0]+1):
    if arr[i]==maxh:
        result += maxh
        maxh = max(arr[i+1:])
        height = maxh
    else:
        if arr[i]>height:
            height=arr[i]
        result += height
print(result)