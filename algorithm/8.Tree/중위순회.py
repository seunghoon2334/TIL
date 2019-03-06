import sys
sys.stdin = open("중위순회.txt")

def inorder(node):
    global result
    if node != 0:
        inorder(tree[node][0])
        result += tree[node][3]
        inorder(tree[node][1])

for tc in range(1,11):
    V = int(input())
    tree = [[0 for _ in range(4)] for _ in range(V+1)]
    result = '#{} '.format(tc)
    for i in range(1,V+1):
        vs = list(input().split())
        if len(vs)==4:
            for ii in range(1,4):
                if ii==1:
                    tree[i][3] = vs[ii]
                elif ii==2:
                    tree[i][0] = int(vs[ii])
                    tree[int(vs[ii])][2] = i
                elif ii==3:
                    tree[i][1] = int(vs[ii])
                    tree[int(vs[ii])][2] = i
        elif len(vs)==3:
            for ii in range(1,3):
                if ii==1:
                    tree[i][3] = vs[ii]
                elif ii==2:
                    tree[i][0] = int(vs[ii])
                    tree[int(vs[ii])][2] = i
        elif len(vs)==2:
            for ii in range(1,2):
                tree[i][3] = vs[ii]

    inorder(1)
    print(result)