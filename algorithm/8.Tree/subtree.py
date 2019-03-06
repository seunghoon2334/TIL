import sys
sys.stdin = open("subtree.txt")

def visit(n):
    if arr[n][0]!=0:
        visited[arr[n][0]] = 1
        visit(arr[n][0])
        if arr[n][1]!=0:
            visited[arr[n][1]] = 1
            visit(arr[n][1])

t = int(input())
for tc in range(t):
    e, n = map(int, input().split())
    visited = [0 for _ in range(e+2)]
    visited[n] = 1
    arr = [[0,0] for _ in range(e+2)]
    node = list(map(int,input().split()))
    for i in range(0,e*2,2):
        if arr[node[i]][0]==0:
            arr[node[i]][0] = node[i+1]
        else:
            arr[node[i]][1] = node[i+1]

    visit(n)
    print('#{} {}'.format(tc+1, visited.count(1)))
