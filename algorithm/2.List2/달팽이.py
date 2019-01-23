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

a = []
for q in range(5):
    a.append([0]*5)
cnt = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
i = 0
ii = 0
p = 0
for t in range(5,0,-2):
    for b in range(t-1):
        a[i][ii] = minsearch(cnt)
        ii += 1
    for c in range(t-1):
        a[i][ii] = minsearch(cnt)
        i += 1
    for d in range(t-1):
        a[i][ii] = minsearch(cnt)
        ii -= 1
    for e in range(t-1):
        a[i][ii] = minsearch(cnt)
        i -= 1
    i += 1
    ii += 1
a[5//2][5//2] = minsearch(cnt)
for i in range(len(a)):
    result = ''
    for ii in range(len(a)):
        result += str(a[i][ii]) + ' '
    print(result)