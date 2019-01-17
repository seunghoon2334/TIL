import sys
sys.stdin = open("sudoku.txt")

t = int(input())
for i in range(t):
    result = 0
    a = []
    b = [[],[],[],[],[],[],[],[],[]]
    c = [[],[],[],[],[],[],[],[],[]]
    d = [[],[],[],[],[],[],[],[],[]]
    for ii in range(9):
        a.append(list(map(int, input().split())))

    d[0].append(a[0][0])
    d[0].append(a[0][1])
    d[0].append(a[0][2])
    d[0].append(a[1][0])
    d[0].append(a[1][1])
    d[0].append(a[1][2])
    d[0].append(a[2][0])
    d[0].append(a[2][1])
    d[0].append(a[2][2])

    d[1].append(a[3][0])
    d[1].append(a[3][1])
    d[1].append(a[3][2])
    d[1].append(a[4][0])
    d[1].append(a[4][1])
    d[1].append(a[4][2])
    d[1].append(a[5][0])
    d[1].append(a[5][1])
    d[1].append(a[5][2])

    d[2].append(a[6][0])
    d[2].append(a[6][1])
    d[2].append(a[6][2])
    d[2].append(a[7][0])
    d[2].append(a[7][1])
    d[2].append(a[7][2])
    d[2].append(a[8][0])
    d[2].append(a[8][1])
    d[2].append(a[8][2])

    d[3].append(a[0][3])
    d[3].append(a[0][4])
    d[3].append(a[0][5])
    d[3].append(a[1][3])
    d[3].append(a[1][4])
    d[3].append(a[1][5])
    d[3].append(a[2][3])
    d[3].append(a[2][4])
    d[3].append(a[2][5])

    d[4].append(a[3][3])
    d[4].append(a[3][4])
    d[4].append(a[3][5])
    d[4].append(a[4][3])
    d[4].append(a[4][4])
    d[4].append(a[4][5])
    d[4].append(a[5][3])
    d[4].append(a[5][4])
    d[4].append(a[5][5])

    d[5].append(a[6][3])
    d[5].append(a[6][4])
    d[5].append(a[6][5])
    d[5].append(a[7][3])
    d[5].append(a[7][4])
    d[5].append(a[7][5])
    d[5].append(a[8][3])
    d[5].append(a[8][4])
    d[5].append(a[8][5])

    d[6].append(a[0][6])
    d[6].append(a[0][7])
    d[6].append(a[0][8])
    d[6].append(a[1][6])
    d[6].append(a[1][7])
    d[6].append(a[1][8])
    d[6].append(a[2][6])
    d[6].append(a[2][7])
    d[6].append(a[2][8])

    d[7].append(a[3][6])
    d[7].append(a[3][7])
    d[7].append(a[3][8])
    d[7].append(a[4][6])
    d[7].append(a[4][7])
    d[7].append(a[4][8])
    d[7].append(a[5][6])
    d[7].append(a[5][7])
    d[7].append(a[5][8])

    d[8].append(a[6][6])
    d[8].append(a[6][7])
    d[8].append(a[6][8])
    d[8].append(a[7][6])
    d[8].append(a[7][7])
    d[8].append(a[7][8])
    d[8].append(a[8][6])
    d[8].append(a[8][7])
    d[8].append(a[8][8])

    for j in range(9):
        for jj in range(9):
            b[j].append(a[j][jj])
            c[j].append(a[jj][j])
    for tt in range(9):
        if len(set(d[tt]))==9 and len(set(b[tt]))==9 and len(set(c[tt]))==9:
            result = 1
        else:
            result = 0
            break
    print(f'#{i+1} {result}')