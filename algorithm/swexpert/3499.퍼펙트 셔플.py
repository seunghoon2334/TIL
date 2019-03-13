import sys
sys.stdin = open("3499.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ns = list(input().split())
    nsa = []
    nsb = []
    result = ''
    if n%2==0:
        for i in range(n//2):
            nsa.append(ns[i])
        for i in range(n//2,n):
            nsb.append(ns[i])
    else:
        for i in range(n//2+1):
            nsa.append(ns[i])
        for i in range(n//2+1,n):
            nsb.append(ns[i])
    for i in range(n//2):
        result += nsa[i] + ' '
        result += nsb[i] + ' '
    if n%2==0:
        print('#{} {}'.format(tc,result))
    else:
        result += nsa[-1] + ' '
        print('#{} {}'.format(tc, result))