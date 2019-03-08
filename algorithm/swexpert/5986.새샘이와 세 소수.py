import sys
sys.stdin = open("5986.txt")

def era(n):
    arr = [0,0] + [1 for _ in range(n-1)]
    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0
    return [i for i in range(len(arr)-1) if arr[i]==1]

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    primes = era(n)
    cnt = 0
    tmp = []
    for x in range(len(primes)-1,-1,-1):
        for y in range(len(primes)-1,-1,-1):
            if primes[x] + primes[y] + 1 >= n:
                pass
            for z in range(len(primes)-1,-1,-1):
                if primes[x]<=primes[y]<=primes[z]:
                    tmp1 = primes[x]
                    tmp2 = primes[y]
                    tmp3 = primes[z]
                elif primes[x]<=primes[z]<=primes[y]:
                    tmp1 = primes[x]
                    tmp2 = primes[z]
                    tmp3 = primes[y]
                elif primes[y]<=primes[x]<=primes[z]:
                    tmp1 = primes[y]
                    tmp2 = primes[x]
                    tmp3 = primes[z]
                elif primes[y]<=primes[z]<=primes[x]:
                    tmp1 = primes[y]
                    tmp2 = primes[z]
                    tmp3 = primes[x]
                elif primes[z]<=primes[x]<=primes[y]:
                    tmp1 = primes[z]
                    tmp2 = primes[x]
                    tmp3 = primes[y]
                elif primes[z]<=primes[y]<=primes[x]:
                    tmp1 = primes[z]
                    tmp2 = primes[y]
                    tmp3 = primes[x]
                if n==tmp1+tmp2+tmp3 and [tmp1,tmp2,tmp3] not in tmp:
                    cnt += 1
                    tmp.append([tmp1,tmp2,tmp3])
    print('#{} {}'.format(tc,cnt))