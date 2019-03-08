import sys
sys.stdin = open("1974.txt")

t = int(input())
for tc in range(1,t+1):
    arr = []
    for i in range(9):
        arr2 = list(map(int, input().split()))
        arr.append(arr2)
    result = 0
    tmp1 = 0
    for i in range(9):
        if len(set(arr[i]))==9:
            tmp1 += 1
    if tmp1==9:
        tmp2 = 0
        for i in range(9):
            check = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(9):
                check[arr[j][i]-1] += 1
            if 0 not in check:
                tmp2 += 1
        if tmp2==9:
            tmp3 = 0
            for i in range(0,9,3):
                for j in range(0,9,3):
                    checklist = [arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j],arr[i+1][j+1],arr[i+1][j+2],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]]
                    if len(set(checklist))==9:
                        tmp3 += 1
            if tmp3==9:
                result = 1
    print('#{} {}'.format(tc,result))