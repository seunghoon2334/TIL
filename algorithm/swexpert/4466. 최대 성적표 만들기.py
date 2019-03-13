import sys
sys.stdin = open("4466.txt")

t = int(input())
for tc in range(1,t+1):
    n, k = map(int, input().split())
    ns = list(map(int, input().split()))
    ns.sort(reverse=True)
    print('#{} {}'.format(tc,sum(ns[:k])))