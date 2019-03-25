import sys
sys.stdin = open("오름차순 정렬(단순정렬).txt")

n = int(input())
nums = list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1,n,1):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
s = ''
for i in range(n):
    s += str(nums[i]) + ' '
print(s)