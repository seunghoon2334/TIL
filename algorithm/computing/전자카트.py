import sys
sys.stdin = open('전자카트.txt')

def myprint(q):
    global result
    tmp = 0
    s = 0
    while q != 0:
        q -= 1
        tmp += arr[s][T[q]]
        if tmp > result:
            return
        s = T[q]
    tmp += arr[s][0]
    if tmp < result:
        result = tmp

def permutation(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1,-1,-1):
            ns[i], ns[n-1] = ns[n-1], ns[i]
            T[r-1] = ns[n-1]
            permutation(n-1, r-1, q)
            ns[i], ns[n-1] = ns[n-1], ns[i]

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = []
    result = 9999
    for i in range(n):
        arr.append(list(map(int,input().split())))
    ns = [i for i in range(1,n)]
    T = [0] * (n-1)
    permutation(n-1, n-1, n-1)
    print('#{} {}'.format(tc,result))