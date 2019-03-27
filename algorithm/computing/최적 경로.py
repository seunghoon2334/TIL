import sys
sys.stdin = open("최적 경로.txt")

def myprint(q):
    global result
    sx = ns[0]
    sy = ns[1]
    p = 0
    while q != 0:
        q -= 1
        p += abs(sx-ns[T[q]]) + abs(sy-ns[T[q]+1])
        sx = ns[T[q]]
        sy = ns[T[q]+1]
        if p > result:
            return
    p += abs(sx-ns[2]) + abs(sy-ns[3])
    if p < result:
        result = p

def permutation(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1,-1,-1):
            a[i], a[n-1] = a[n-1], a[i]
            T[r-1] = a[n-1]
            permutation(n-1, r-1, q)
            a[i], a[n-1] = a[n-1], a[i]

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    ns = list(map(int,input().split()))
    a = [i for i in range(4,2*((len(ns))//2),2)]
    T = [0] * n
    result = 9999
    permutation(n, n, n)

    print('#{} {}'.format(tc,result))