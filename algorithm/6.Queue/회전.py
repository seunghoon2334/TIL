import sys
sys.stdin = open('회전.txt')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    m %= n
    print(f'#{tc+1} {arr[m]}')