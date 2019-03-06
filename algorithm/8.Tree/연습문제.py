import sys
sys.stdin = open("연습문제.txt")

v = int(input())
tree = [[0,0,0] for _ in range(v+1)]
edge = list(map(int, input().split()))
for i in range(v-1):
    if tree[edge[i*2]][0]==0:
        tree[edge[i * 2]][0] = edge[(i*2)+1]
    else:
        tree[edge[i * 2]][1] = edge[(i*2)+1]
    tree[edge[(i*2)+1]][2] = edge[i*2]

for i in range(1,v+1):
    print(i, tree[i][0], tree[i][1], tree[i][2])

for i in range(1,v+1):
    if tree[i][2]==0:
        root = i
        break

# result = [root]
# while len(result)!=v: #전위
#     if tree[root][0]!=0:
#         tmp = tree[root][0]
#         tree[root][0] = 0
#         root = tmp
#         result.append(root)
#     elif tree[root][1]!=0:
#         tmp = tree[root][1]
#         tree[root][1] = 0
#         root = tmp
#         result.append(root)
#     else:
#         root = tree[root][2]
# print(result)

start = root

while tree[start][0]!=0:
    start = tree[start][0]
print(start)
result = []
while len(result)!=v: #중위
    if tree[start][0]==0 and tree[start][1]==0:
        result.append(start)
        tmp = tree[start][2]
        if tree[tmp][0] == start:
            tree[tmp][0] = 0
        else:
            tree[tmp][1] = 0
        start = tmp
    elif tree[start][0]==0 and tree[start][1]!=0:
        result.append(start)
        tmp = tree[start][1]

        tree[start][1] = 0
        start = tmp
    else:
        start = tree[start][0]

print(result)