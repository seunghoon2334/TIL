import sys
sys.stdin = open("2409파이프 자르기.txt")

m = int(input())
ms = list(map(int, input().split()))
n = int(input())
ns = list(map(int, input().split()))

ms.sort(reverse=True)
ns.sort()

j = 0
for i in range(m):
    while True:
        if ms[i]>ns[j]:
            ms[i] -= ns[j]
            ns[j] = 0
            j += 1
        else:
            break
        if j==n:
            break
    if j == n:
        break
print(ns.count(0))