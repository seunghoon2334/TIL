import sys
sys.stdin = open("color.txt")

t = int(input())
for tc in range(t):
    num = int(input())
    cnt = 0
    arr = []
    for i in range(10):
        arr.append([0] * 10)
    for n in range(num):
        x1, y1, x2, y2, c = map(int, input().split())
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                arr[x][y] += c
    for i in range(10):
        for j in range(10):
            if arr[i][j]==3:
                cnt += 1
    print(f'#{tc+1} {cnt}')