import sys
sys.stdin = open('3260.txt')

t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    print('#{} {}'.format(tc,a+b))