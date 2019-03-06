import sys
sys.stdin = open("e0수열.txt")

n = int(input())
nums = list(map(int, input().split()))

result1 = 0
cnt1 = 1
for i in range(n-1):
    if nums[i]<=nums[i+1]:
        cnt1 += 1
    else:
        if cnt1>result1:
            result1 = cnt1
        cnt1 = 1
if cnt1>result1:
    result1 = cnt1

result2 = 0
cnt2 = 1
for i in range(n-1):
    if nums[i]>=nums[i+1]:
        cnt2 += 1
    else:
        if cnt2>result2:
            result2 = cnt2
        cnt2 = 1
if cnt2>result2:
    result2 = cnt2

print(max(result1,result2))