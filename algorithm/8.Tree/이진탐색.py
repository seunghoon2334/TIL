import sys
sys.stdin = open("이진탐색.txt")

def inorder(node):
    global result
    if node != 0:
        inorder(tree[node][0])
        if node not in result:
            result.append(node)
        inorder(tree[node][1])

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    tree = [[0,0,0,0] for _ in range(n+1)]

    for i in range(1,n+1):
        tree[i][2] = i//2
        if tree[i//2][0]==0:
            tree[i//2][0] = i
        else:
            tree[i//2][1] = i
    result = [0]
    inorder(1)
    print('#{} {} {}'.format(tc,result.index(1),result.index(n//2)))