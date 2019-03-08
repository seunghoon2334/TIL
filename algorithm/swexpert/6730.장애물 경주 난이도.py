import sys
sys.stdin = open("6730.txt")

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    ns = list(map(int, input().split()))
    up = [0]
    down = [0]
    for i in range(n-1):
        if ns[i]<ns[i+1]:
            up.append(ns[i+1]-ns[i])
        elif ns[i]>ns[i+1]:
            down.append(ns[i]-ns[i+1])
    print('#{} {} {}'.format(tc, max(up), max(down)))