import sys
sys.stdin = open("사칙연산.txt")

def order(n):
    if tree[n][3]=='-':
        return order(tree[n][0]) - order(tree[n][1])
    elif tree[n][3]=='+':
        return order(tree[n][0]) + order(tree[n][1])
    elif tree[n][3]=='*':
        return order(tree[n][0]) * order(tree[n][1])
    elif tree[n][3]=='/':
        return order(tree[n][0]) // order(tree[n][1])
    else:
        return tree[n][3]

for tc in range(1,11):
    V = int(input())
    tree = [[0,0,0,0] for _ in range(V+1)] #자식1,2,부모,값
    for i in range(V):
        s = list(input().split())
        if len(s)==4:
            tree[int(s[0])][3] = s[1]
            tree[int(s[0])][0] = int(s[2])
            tree[int(s[2])][2] = int(s[0])
            tree[int(s[0])][1] = int(s[3])
            tree[int(s[3])][2] = int(s[0])
        elif len(s)==2:
            tree[int(s[0])][3] = int(s[1])
    print('#{} {}'.format(tc,order(1)))
