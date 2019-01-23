'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
# 정답 : 24
def isWall(x, y):
    if x<0 or y<0 or x>4 or y>4:
        return False
    else:
        return True

def calAbs(x, y):
    if x>=y:
        return x-y
    else:
        return y-x

def myAbs(a):
    if a>0:
        return a
    return -a

arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [0, 0, -1, 1]#상하좌우
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            textX = x + dx[i]
            textY = y + dy[i]
            if isWall(textX, textY):
                sum += calAbs(arr[x][y], arr[textX][textY])
print(sum)
