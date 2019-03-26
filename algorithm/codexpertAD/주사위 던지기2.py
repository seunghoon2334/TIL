import sys
sys.stdin = open('주사위 던지기2.txt')

def myprint(q):
    tmp = 0
    t = []
    while q != 0:
        q -= 1
        t.append(T[q])
        tmp += T[q]
        if tmp>m:
            break
    if tmp==m:
        result.append(t)

def PI(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1,-1,-1):
            arr[i], arr[n-1] = arr[n-1], arr[i]
            T[r-1] = arr[n-1]
            PI(n, r-1, q)
            arr[i], arr[n-1] = arr[n-1], arr[i]

n, m = map(int,input().split())
arr = [1,2,3,4,5,6]
T = [0] * n
result = []
PI(6, n, n)
result.sort()
for i in range(len(result)):
    print(' '.join(map(str, result[i])))