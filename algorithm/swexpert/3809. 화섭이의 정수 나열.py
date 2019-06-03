import sys
sys.stdin = open('3809.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    ns = ''

    while True:
        ns += ''.join(input().split())
        if len(ns)==n:
            break

    cnt = 0
    while cnt<1001:
        if str(cnt) in ns:
            cnt += 1
        else:
            break

    result = cnt

    print('#{} {}'.format(tc, result))