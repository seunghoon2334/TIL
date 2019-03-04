n = int(input())
anum = []
bnum = []
cnum = []
for nc in range(n):
    a, b, c = map(int, input().split())
    anum.append(a)
    bnum.append(b)
    cnum.append(c)
for i in range(n):
    result = 0
    if anum.count(anum[i])==1:
        result += anum[i]
    if bnum.count(bnum[i])==1:
        result += bnum[i]
    if cnum.count(cnum[i])==1:
        result += cnum[i]
    print(result)