import sys
sys.stdin = open("사칙연산.txt")

def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        tmp.append(node)

for tc in range(1,11):
    V = int(input())
    tree = [[0,0,0] for _ in range(V+1)] #자식1,2,부모,값
    for i in range(V):
        s = list(input().split())
        if len(s)==4:
            tree[int(s[0])][2] = s[1]
            tree[int(s[0])][0] = int(s[2])
            tree[int(s[0])][1] = int(s[3])
        elif len(s)==2:
            tree[int(s[0])][2] = int(s[1])
    tmp = []
    postorder(1)
    stack = []
    for i in range(len(tmp)):
        if tree[tmp[i]][2]=='+':
            tmp2 = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp1 + tmp2)
        elif tree[tmp[i]][2]=='-':
            tmp2 = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp1 - tmp2)
        elif tree[tmp[i]][2]=='*':
            tmp2 = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp1 * tmp2)
        elif tree[tmp[i]][2]=='/':
            tmp2 = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp1 / tmp2)
        else:
            stack.append(tree[tmp[i]][2])
    print('#{} {}'.format(tc,int(stack[0])))