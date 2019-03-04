def search(num):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = 0

def cross():
    result = 0
    cnt = 0
    for i in range(5):
        if arr[i][i] == 0:
            cnt += 1
        else:
            break
    if cnt == 5:
        result += 1
    cnt = 0
    for i in range(5):
        if arr[i][4 - i] == 0:
            cnt += 1
        else:
            break
    if cnt == 5:
        result += 1
    return result

def row():
    result = 0
    for i in range(5):
        if arr[i].count(0) == 5:
            result += 1
    return result

def col():
    result = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if arr[j][i] == 0:
                cnt += 1
        if cnt == 5:
            result += 1
    return result

arr = []
check = []
for _ in range(5):
    arr.append(list(map(int, input().split())))
for _ in range(5):
    check.append(list(map(int, input().split())))
cnt = 0
i = 0
j = 0
bingo = 0
while cnt < 25:
    search(check[i][j])
    j += 1
    if j == 5:
        j = 0
        i += 1
    cnt += 1
    crosspoint = cross()
    rowpoint = row()
    colpoint = col()
    bingo = crosspoint + rowpoint + colpoint
    if bingo >= 3:
        break
print(cnt)