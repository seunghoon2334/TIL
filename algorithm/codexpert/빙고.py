
def find_clear(num):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
                return

def bingo_count():
    cnt = 0
    tot1, tot2, tot3, tot4 = 0, 0, 0, 0
    for i in range(5):
        tot1, tot2 = 0, 0
        for j in range(5):
            tot1 += bingo[i][j]
            tot2 += bingo[j][i]
        if tot1 == 0:
           cnt += 1
        if tot2 == 0:
            cnt += 1
        # cnt += not tot1
        # cnt += not tot2
        tot3 += bingo[i][i]
        tot4 += bingo[i][4 - i]
    cnt += not tot3
    cnt += not tot4
    return cnt

def mc_call(num):
    find_clear(num)
    if bingo_count() >= 3:
        return 1
    return 0

bingo = []
for i in range(5):
    bingo.append(list(map(int, input().split())))
mc = []
for i in range(5):
    mc.append(list(map(int, input().split())))
for i in range(25):
    if mc_call(mc[i // 5][i % 5]):
        break
print(i + 1)