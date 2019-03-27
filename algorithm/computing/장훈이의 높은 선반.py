import sys
sys.stdin = open('장훈이의 높은 선반.txt')

def myprint(q):
    global result
    tmp = 0
    while q != 0:
        q -= 1
        tmp += T[q]
    if b <= tmp < result:
        result = tmp

def combination(n, r, q):
    if r == 0:
        myprint(q)
    elif n < r:
        return
    else:
        T[r-1] = ns[n-1]
        combination(n-1, r-1, q)
        combination(n-1, r, q)

t = int(input())
for tc in range(1,t+1):
    n, b = map(int,input().split())
    ns = list(map(int,input().split()))
    T = [0] * n
    result = 200000
    for i in range(n, 1, -1):
        combination(n, i, i)

    print('#{} {}'.format(tc,result-b))