import sys
sys.stdin = open("palin.txt")

def palin(a):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    s = []
    result = ''
    for i in range(n):
        s.append(input())

    for i in range(n):
        for ii in range(0,n-m+1):
            if palin(s[i][ii:ii+m]): #가로로 m길이만큼 확인
                result = s[i][ii:ii+m]
                break
        if result != '':
            print(f'#{tc+1} {result}')
            break

        for ii in range(n-m+1):
            ss = ''
            for iii in range(m):
                ss += s[ii+iii][i]
            if palin(ss):
                result = ss
                break
        if result != '':
            print(f'#{tc+1} {result}')
            break