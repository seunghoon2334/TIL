import sys
sys.stdin = open('3456.txt')

t = int(input())
for tc in range(1,t+1):
    a,b,c = map(int,input().split())
    if a==b:
        result = c
    elif a==c:
        result = b
    else:
        result = a

    print('#{} {}'.format(tc, result))