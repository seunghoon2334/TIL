import sys
sys.stdin = open("e2참외 밭(중등).txt")

n = int(input())
ab6 = []
result2 = 1
for i in range(6):
    a, b = map(int, input().split())
    ab6.append([a,b])

ab11 = []
for i in range(11):
    if i<=5:
        ab11.append(ab6[i])
    else:
        ab11.append(ab6[i-6])
for i in range(6):
    s = str(ab11[i][0]) + str(ab11[i+1][0]) + str(ab11[i+2][0]) + str(ab11[i+3][0]) + str(ab11[i+4][0]) + str(ab11[i+5][0])
    if s=='231314':
        ab = ab11[i:i+6]
        break
    elif s=='314142':
        ab = ab11[i:i + 6]
        break
    elif s=='142423':
        ab = ab11[i:i + 6]
        break
    elif s=='423231':
        ab = ab11[i:i + 6]
        break

result = (ab[0][1]*ab[5][1]) - (ab[2][1]*ab[3][1])
print(result*n)