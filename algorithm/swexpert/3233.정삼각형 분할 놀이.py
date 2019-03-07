import sys
sys.stdin = open("3233.txt")

def tri(n):
    cnt = 1
    result = 0
    for i in range(n):
        result += cnt
        cnt += 2
    return result

t = int(input())
for tc in range(1,t+1):
    a, b = map(int, input().split())
    print('#{} {}'.format(tc, tri(a//b)))