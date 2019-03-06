import sys
sys.stdin = open("d3나는 학급회장이다.(투표).txt")

n = int(input())
arr = [[0,0,0],[0,0,0],[0,0,0]] #abc 1점2점3점
asum = 0
bsum = 0
csum = 0
for i in range(n):
    a, b, c = map(int,input().split())
    asum += a
    bsum += b
    csum += c
    arr[0][a-1] += 1
    arr[1][b-1] += 1
    arr[2][c-1] += 1
# print(asum,bsum,csum)
# print(arr)

if asum<bsum:
    if bsum<csum:
        print(3, csum)
    elif bsum==csum:
        if arr[1][2]==arr[2][2]:
            if arr[1][1]==arr[2][1]:
                if arr[1][0]==arr[2][0]:
                    print(0, bsum)
                elif arr[1][0]>arr[2][0]:
                    print(2, bsum)
                else:
                    print(3, csum)
            elif arr[1][1]>arr[2][1]:
                print(2, bsum)
            else:
                print(3, csum)
        elif arr[1][2]>arr[2][2]:
            print(2, bsum)
        else:
            print(3,csum)
    else:
        print(2, bsum)
elif asum==bsum:
    if asum<csum:
        print(3, csum)
    elif asum==csum:
        if arr[0][2]==arr[2][2]:
            if arr[0][1]==arr[2][1]:
                if arr[0][0]==arr[2][0]:
                    if arr[2][2]==arr[1][2]:
                        if arr[2][1]==arr[1][1]:
                            if arr[2][0]==arr[1][0]:
                                print(0, csum)
                            elif arr[2][1]>arr[1][1]:
                                print(3, csum)
                            else:
                                print(2, bsum)
                        elif arr[2][1]>arr[1][1]:
                            print(3, csum)
                        else:
                            print(2, bsum)
                    elif arr[2][2]>arr[1][2]:
                        print(3, csum)
                    else:
                        print(2, bsum)
                elif arr[0][0]>arr[2][0]:
                    if arr[2][2]==arr[0][2]:
                        if arr[2][1]==arr[0][1]:
                            if arr[2][0]==arr[0][0]:
                                print(0, asum)
                            elif arr[2][1]>arr[0][1]:
                                print(3, csum)
                            else:
                                print(2, asum)
                        elif arr[2][1]>arr[0][1]:
                            print(3, csum)
                        else:
                            print(2, asum)
                else:
                    if arr[2][2]==arr[1][2]:
                        if arr[2][1]==arr[1][1]:
                            if arr[2][0]==arr[1][0]:
                                print(0, bsum)
                            elif arr[2][1]>arr[1][1]:
                                print(3, csum)
                            else:
                                print(2, bsum)
                        elif arr[2][1]>arr[1][1]:
                            print(3, csum)
                        else:
                            print(2, bsum)
            elif arr[0][1]>arr[2][1]:
                if arr[0][2] == arr[1][2]:
                    if arr[0][1] == arr[1][1]:
                        if arr[0][0] == arr[1][0]:
                            print(0, bsum)
                        elif arr[0][1] > arr[1][1]:
                            print(1, asum)
                        else:
                            print(2, bsum)
                    elif arr[0][1] > arr[1][1]:
                        print(1, asum)
                    else:
                        print(2, bsum)
            else:
                if arr[2][2] == arr[1][2]:
                    if arr[2][1] == arr[1][1]:
                        if arr[2][0] == arr[1][0]:
                            print(0, bsum)
                        elif arr[2][1] > arr[1][1]:
                            print(3, csum)
                        else:
                            print(2, bsum)
                    elif arr[2][1] > arr[1][1]:
                        print(3, csum)
                    else:
                        print(2, bsum)
        elif arr[0][2]>arr[2][2]:
            if arr[2][2] == arr[0][2]:
                if arr[2][1] == arr[0][1]:
                    if arr[2][0] == arr[0][0]:
                        print(0, asum)
                    elif arr[2][1] > arr[0][1]:
                        print(3, csum)
                    else:
                        print(1, asum)
                elif arr[2][1] > arr[0][1]:
                    print(3, csum)
                else:
                    print(1, asum)
        else:
            if arr[2][2] == arr[1][2]:
                if arr[2][1] == arr[1][1]:
                    if arr[2][0] == arr[1][0]:
                        print(0, csum)
                    elif arr[2][1] > arr[1][1]:
                        print(3, csum)
                    else:
                        print(2, bsum)
                elif arr[2][1] > arr[1][1]:
                    print(3, csum)
                else:
                    print(2, bsum)
            elif arr[2][2]>arr[1][2]:
                print(3, csum)
            else:
                print(2, bsum)
    else:
        if arr[0][2] == arr[1][2]:
            if arr[0][1] == arr[1][1]:
                if arr[0][0] == arr[1][0]:
                    print(0, asum)
                elif arr[0][1] > arr[1][1]:
                    print(1, asum)
                else:
                    print(2, bsum)
            elif arr[0][1] > arr[1][1]:
                print(1, asum)
            else:
                print(2, bsum)
        elif arr[0][2]>arr[1][2]:
            print(1, asum)
        else:
            print(2, bsum)

else:
    if asum<csum:
        print(3, csum)
    elif asum==csum:
        if arr[0][2]==arr[2][2]:
            if arr[0][1]==arr[2][1]:
                if arr[0][0]==arr[2][0]:
                    print(0, csum)
                elif arr[0][0]>arr[2][0]:
                    print(1, asum)
                else:
                    print(3, csum)
            elif arr[0][1]>arr[2][0]:
                print(1, asum)
            else:
                print(3, csum)
        elif arr[0][2]>arr[2][2]:
            print(1, asum)
        else:
            print(3, csum)
    else:
        print(1, asum)