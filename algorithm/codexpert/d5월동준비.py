import sys
sys.stdin = open("d5월동준비.txt")

acorn = int(input())
acorns = list(map(int, input().split()))

tmp1 = 0
tmp2 = acorns[0]
result1 = -99999
for i in range(acorn):
    tmp2 = acorns[i]
    tmp1 = max(tmp1+acorns[i], tmp2)
    if tmp1>result1:
        result1 = tmp1

result2 = 0
cnt = 0
for i in range(len(acorns)):
    if acorns[i]>0:
        result2 += acorns[i]
    else:
        cnt += 1
if cnt==len(acorns):
    result2 = max(acorns)
print(result1, result2)