import sys
sys.stdin = open('최소 비용으로 포장 다시하기.txt')

n = int(input())
ns = list(map(int,input().split()))
cnt = 0
for i in range(n-1):
    for j in range(i,i+2):
        for k in range(j,n):
            if ns[j] > ns[k]:
                ns[j], ns[k] = ns[k], ns[j]

    ns[i+1] += ns[i]
    cnt += ns[i+1]
print(cnt)