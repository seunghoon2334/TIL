def BFS():
    que = []
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    que.append((sr, sc, 0))
    arr[sr][sc] = 1

    while que:
        r, c, time = que.pop(0)
        if r==er and c == ec : return time # 도착했으면 리턴
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if(nr<1 or nc<1 or nr>R or nc>C): continue # 맵범위 체크
            if arr[nr][nc] !=0 : continue # 길이아니면 스킵
            que.append((nr, nc, time+1))
            arr[nr][nc]=1
    return -1 # 예외처리(더이상 갈길이 없다면)


# main ========================================
C, R = map(int, input().split())
arr = [ [0] * (C+2) for _ in range(R+2)]
sc, sr, ec, er = map(int, input().split())

for i in range(1, R+1):
    temp = input()
    for j in range(1, C+1):
        arr[i][j] = int(temp[j-1])

sol = BFS()
print(sol)