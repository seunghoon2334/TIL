import sys
sys.stdin = open("공통조상.txt")

def search(n):
    global cnt
    if tree[n][1]!=0:
        search(tree[n][0])
        search(tree[n][1])
        cnt += 1
    elif tree[n][0]!=0:
        search(tree[n][0])
        cnt += 1
    else:
        cnt += 1


t = int(input())
for tc in range(1,t+1):
    V, E, v1, v2 = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]

    vs = list(map(int, input().split())) #부모 자식
    for i in range(E):
        if tree[vs[i*2]][0]==0:
            tree[vs[i*2]][0] = vs[(i*2)+1]
        else:
            tree[vs[i*2]][1] = vs[(i*2)+1]
        tree[vs[(i*2)+1]][2] = vs[i*2]


    result1 = []
    while tree[v1][2]!=0:
        result1.append(tree[v1][2])
        v1 = tree[v1][2]
    while tree[v2][2]!=0:
        if tree[v2][2] in result1:
            result2 = tree[v2][2]
            break
        v2 = tree[v2][2]
    cnt = 0
    search(result2)
    print('#{} {} {}'.format(tc,result2,cnt))

