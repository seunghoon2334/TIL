import sys
sys.stdin = open("190227workshop.txt")

t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for nc in range(n):
        arr.append(list(map(int, input().split())) + [0])
    arr.append([0]*(n+1))
    visited = [[0 for _ in range(n+1)] for _ in range(n+2)]
    q = []
    # for i in range(n+1):
    #     print(arr[i])
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and arr[i][j]!=0:
                visited[i][j]=1
                starti = i
                startj = j
                while arr[starti][startj]!=0:
                    startj += 1
                startj -= 1
                endj = startj
                while arr[starti][endj]!=0:
                    starti += 1
                starti -= 1
                endi = starti
                if i==endi and j==endj:
                    q.append([1,i,j])
                elif i==endi and j!=endj:
                    q.append([endj-j+1,1,endj-j+1])
                elif i!=endi and j==endj:
                    q.append([endi-i+1,endi-i+1,1])
                else:
                    q.append([(endi-i+1)*(endj-j+1),endi-i+1,endj-j+1])
                for ii in range(i,endi+1):
                    for jj in range(j,endj+1):
                        visited[ii][jj] = 1
    # print(q)
    # print()

    q.sort()
    # print(q)
    result = ''
    for i in range(len(q)):
        result += ' ' + str(q[i][1]) + ' ' + str(q[i][2])
    print(f'#{tc+1} {len(q)}{result}')
