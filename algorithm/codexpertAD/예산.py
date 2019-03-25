import sys
sys.stdin = open("예산.txt")

def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

n = int(input())
ns = list(map(int,input().split()))
ns = merge_sort(ns)
m = int(input())
result = 0
tmp = ns[-1]
for i in range(n):
    result += ns[i]
if result<=m:
    print(tmp)
else:
    check = 0
    for i in range(n):
        if ns[i]<=m/(n-i):
            check = i
            m -= ns[i]
        else:
            break
    print(m//(n-i))