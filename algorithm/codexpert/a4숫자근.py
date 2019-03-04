n = int(input())
cnt = 0
result = 0

m = []
for nc in range(n):
    m.append(int(input()))
m.sort()
for i in range(n):
    num = str(m[i])
    while len(num) != 1:
        tmp = 0
        for ii in num:
            tmp += int(ii)
        num = str(tmp)
    if int(num) > cnt:
        cnt = int(num)
        result = m[i]
print(result)