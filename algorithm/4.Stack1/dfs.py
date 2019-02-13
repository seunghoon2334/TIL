import sys
sys.stdin = open("연습3_input.txt")

V, E = map(int, input().split())
n = list(map(int, input().split()))
visited = [0 for i in range(V+1)]
arr = []

for i in range(E):
    arr.append([0] * (E))

for i in range(0,E*2,2):
    arr[n[i]][n[i+1]] = 1
    arr[n[i+1]][n[i]] = 1

for i in range(E):
    print(arr[i])

def dfs(v):
    global arr, V, visited
    visited[v] = 1
    


# i=0
# j=0
# cnt=1
# while True:
#     if arr[i][j]==1:
#         if visited[i]!=1:
#             print(i)
#             visited[i] = 1
#         i = j
#         j = 0
#     else:
#         j+=1
#         if j == E:
#             i+=1
#             j=0
#             if i==E:
#                 i-=cnt
#                 cnt+=1
#     if cnt==E:
#         cnt=0
#     if not 0 in visited:
#         break




