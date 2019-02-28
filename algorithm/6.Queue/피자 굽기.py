import sys
sys.stdin = open('피자 굽기.txt')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split()) #화덕,피자
    cheeze = list(map(int, input().split()))
    pizza = 0
    q = [0]*n
    result = []
    inoven = [0]*n
    while len(result)!=m:
        for i in range(n):
            if q[i]==0 and pizza!=m:
                q[i] = cheeze[pizza]
                inoven[i] = pizza
                pizza += 1
                q[i] //= 2
                if q[i]==0:
                    result.append(inoven[i])
                    inoven[i] = 0
            else:
                q[i] //= 2
                if q[i]==0 and inoven[i] not in result:
                    result.append(inoven[i])
                    inoven[i] = 0

    print(f'#{tc+1} {result[-1]+1}')






