import sys
sys.stdin = open("190131workshop.txt")

def palin(a):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True

for q in range(10):
    t = int(input())
    n = 100
    m = 100
    result = ''
    s = []
    for i in range(n):
        s.append(input())

    while result=='':
        for i in range(n):
            for ii in range(0,n-m+1):
                if palin(s[i][ii:ii+m]): #가로로 m길이만큼 확인
                    result = s[i][ii:ii+m]
                    break
            if result != '':
                break

            for ii in range(n-m+1):
                ss = ''
                for iii in range(m):
                    ss += s[ii+iii][i]
                if palin(ss):
                    result = ss
                    break
            if result != '':
                break
        m -= 1
    print(f'#{t} {len(result)}')