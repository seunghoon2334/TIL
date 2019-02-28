node = 7
edge = 8
arr = [[0 for _ in range(node+1)] for _ in range(node+1)]

edges = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
for i in range(0,2*edge,2):
    arr[edges[i]][edges[i+1]] = 1
    arr[edges[i+1]][edges[i]] = 1
# for i in range(edge):
#     print(arr[i])
# print()

start = 1
visit = [1] + [0]*node
q = []

while visit!=[1]*(node+1) or q!=[]:
    if visit[start]==0:
        visit[start]=1
        print(start)
        for i in range(1,node+1):
            if arr[start][i]==1 and visit[i]==0 and (i not in q):
                q.append(i)
    else:
        arr[start][q[0]]=0
        arr[q[0]][start]=0
        start = q[0]
        q.pop(0)