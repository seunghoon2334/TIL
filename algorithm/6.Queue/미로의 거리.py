import sys
sys.stdin = open('미로의 거리.txt')

def isWall(i,j):
    global cnt
    tmp = 0
    if maze[i-1][j]==1:
        tmp += 1
    if maze[i][j+1]==1:
        tmp += 1
    if maze[i+1][j]==1:
        tmp += 1
    if maze[i][j-1]==1:
        tmp += 1
    if tmp==4:
        return False
    elif tmp==2 or tmp==1:
        stack.append([i,j,cnt])
        return True
    else:
        return True

def go(i,j):
    global cnt
    if maze[i-1][j]!=1:
        i -= 1
        cnt += 1
        return [i,j]
    elif maze[i][j+1]!=1:
        j += 1
        cnt += 1
        return [i,j]
    elif maze[i+1][j]!=1:
        i += 1
        cnt += 1
        return [i,j]
    elif maze[i][j-1]!=1:
        j -= 1
        cnt += 1
        return [i,j]

t = int(input())
for tc in range(t):
    n = int(input())
    maze = [[1 for _ in range(n+2)]]
    cnt = 0
    for i in range(n):
        m = input()
        m2 = [1]
        for ii in range(n):
            if m[ii]=='2':
                starti=i+1
                startj=ii+1
            m2.append(int(m[ii]))
        m2.append(1)
        maze.append(m2)
    maze.append([1 for _ in range(n+2)])
    stack = [[starti,startj,cnt]]

    # for i in range(n+2):
    #     print(maze[i])

    i = starti
    j = startj
    result = []
    while True:
        maze[i][j] = 1
        if not isWall(i,j):
            i = stack[-1][0]
            j = stack[-1][1]
            cnt = stack[-1][2]
            stack.pop()
        else:
            new = go(i,j)
            i = new[0]
            j = new[1]
        if stack==[] and not isWall(i,j):
            cnt = 0
            break
        elif maze[i][j]==3:
            cnt -= 1
            break

    print(f'#{tc+1} {cnt}')