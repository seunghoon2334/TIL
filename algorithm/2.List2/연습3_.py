def minsearch(data):
    minv = data[0][0]
    a = 0
    b = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if minv > data[i][j]:
                minv = data[i][j]
                a = i
                b = j
    data[a][b] = 99
    return minv

def isWall(x, y):
    if x<0 or y<0 or x>4 or y>4:
        return True
    else:
        return False


data = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
dx = [0, 1, 0, -1]#상하좌우
dy = [1, 0, -1, 0]
# dx = [0, 0, -1, 1]#상하좌우
# dy = [-1, 1, 0, 0]
arr = []
for q in range(5):
    arr.append([0]*5)

x=0
y=0
for ii in range(25):
    for i in range(4):
        if isWall(x,y) or isWall(x,y)!=0:#벽이거나 0이 아니면
            if i%2==0:
                y -= dy[i]
            else:
                x -= dx[i]
        else:
            arr[x][y] = minsearch(data)

            if i%2==0:
                y += dy[i]
            else:
                x += dx[i]
            break

print(arr)




