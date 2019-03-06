import sys
sys.stdin = open("노드의 합.txt")


def treeres(n):
    if tree[n][0]==0 and tree[n][1]==0:
        return 0
    elif tree[n][0]!=0 and tree[n][1]==0:
        tree[n][2] = tree[tree[n][0]][2]
    else:
        tree[n][2] = tree[tree[n][0]][2] + tree[tree[n][1]][2]

t = int(input())
for tc in range(1, t+1):
    N, M, L = map(int, input().split()) #노드개수,리프노드개수,출력할노드번호
    tree = [[0,0,0] for _ in range(N+1)]
    for i in range(2,N+1):
        if tree[i//2][0]==0:
            tree[i//2][0] = i
        else:
            tree[i//2][1] = i

    for mc in range(M):
        num, res = map(int,input().split())
        tree[num][2] = res

    for i in range(N,0,-1):
        treeres(i)
    print('#{} {}'.format(tc,tree[L][2]))