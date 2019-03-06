import sys
sys.stdin = open("c5반나누기.txt")

t = int(input())
for tc in range(t):
    n, kmin, kmax = map(int, input().split()) #신입,최소,최대

    nscore = list(map(int, input().split()))
    nscore.sort()
    result = []
    for i in range(1,100):
        for j in range(2,101):
            if i<j:
                a = 0
                b = 0
                c = 0
                for ii in range(n):
                    if nscore[ii]<i:
                        a += 1
                        if a>kmax:
                            break
                    elif i<=nscore[ii]<j:
                        b += 1
                        if b>kmax:
                            break
                    else:
                        c += 1
                        if c>kmax:
                            break
                if kmin<=a<=kmax and kmin<=b<=kmax and kmin<=c<=kmax :
                    result.append([a,b,c])
    if len(result)==0:
        print(-1)
    else:
        result2 = 1001
        for i in range(len(result)):
            if max(result[i]) - min(result[i]) < result2:
                result2 = max(result[i]) - min(result[i])
        print(result2)