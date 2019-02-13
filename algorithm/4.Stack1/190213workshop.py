import sys
sys.stdin = open("190213workshop.txt")


for tc in range(10):
    arr = []
    tttt = input()
    for i in range(100):
        arr.append(list(map(int, input().split())))

    x = arr[99].index(2)
    y = 99
    cnt = 0
    while y!=0:
        if x!=0 and x!=99:
            if arr[y][x-1]==1:
                arr[y][x] = 0
                x -= 1
            elif arr[y][x+1]==1:
                arr[y][x] = 0
                x += 1
            else:
                arr[y][x] = 0
                y -= 1
        elif x==0:
            if arr[y][x+1]==1:
                arr[y][x] = 0
                x += 1
            else:
                arr[y][x] = 0
                y -= 1
        elif x==99:
            if arr[y][x-1]==1:
                arr[y][x] = 0
                x -= 1
            else:
                arr[y][x] = 0
                y -= 1
    print(f'#{tttt} {x}')