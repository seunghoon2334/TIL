import sys
sys.stdin = open("종이붙이기.txt")

def fac(n):
    f = [1, 1]
    for i in range(2, n+1):
        f.append(f[i-1] * i)
    return f[n]

def combi(n,r):
    return fac(n)//(fac(r) * fac(n-r))

def square(n):
    n = n//10
    result = 0
    cnt = 0

    for r in range(n,-1,-2):
        result += (combi(n,r) * (2**cnt))
        cnt += 1
        n -= 1

    return result

t = int(input())
for tc in range(t):
    n = int(input())
    print(f'#{tc+1} {square(n)}')