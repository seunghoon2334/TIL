import sys
sys.stdin = open('6057.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    array = [[] for _ in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        array[x-1].append(y-1)
        array[y-1].append(x-1)
    cnt = 0
    for i in range(n):
        for j in range(len(array[i])):
            tmp1 = array[array[i][j]]
            for k in range(len(tmp1)):
                tmp2 = array[tmp1[k]]
                for l in range(len(tmp2)):
                    if i==tmp2[l]:
                        cnt += 1
    print('#{} {}'.format(tc, cnt//6))