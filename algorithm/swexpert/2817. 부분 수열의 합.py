import sys
import itertools
sys.stdin = open('2817.txt')

t = int(input())
for tc in range(1, t+1):
    n, point = map(int, input().split())
    ns = list(map(int, input().split()))
    cnt = 0
    for i in range(n, 0, -1):
        combi = list(itertools.combinations(ns, i))
        for j in range(len(combi)):
            tmp = 0
            for k in range(i):
                tmp += combi[j][k]
                if tmp > point:
                    break
            if tmp==point:
                cnt += 1
    print('#{} {}'.format(tc,cnt))