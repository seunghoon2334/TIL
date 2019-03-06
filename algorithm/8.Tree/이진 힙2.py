import sys
sys.stdin = open("이진 힙.txt")

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    ns = list(map(int, input().split()))
    tree = [[0,0,0,0] for _ in range(n+1)]
    for i in range(1,n+1):
        tree[i][2] = i//2
        if tree[i//2][0]==0:
            tree[i//2][0] = i
        else:
            tree[i//2][1] = i
    tree[0][0] = 0

    for i in range(1,n+1):
        tree[i][3] = ns[i-1]
        while tree[i][3]<tree[tree[i][2]][3]:
            tree[i][3],tree[tree[i][2]][3] = tree[tree[i][2]][3],tree[i][3]
            i = tree[i][2]
    result = 0
    tmp = n
    while tree[n][2]!=0:
        n = tree[n][2]
        result += tree[n][3]
    print('#{} {}'.format(tc,result))