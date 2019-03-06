r = int(input())

cnt = 0
for i in range(r):
    if ((i + 1) ** 2) * 2 <= r ** 2:
        cnt += 1
    for j in range(i + 1, r):
        if (i + 1) ** 2 + (j + 1) ** 2 <= r ** 2:
            cnt += 2
print(cnt * 4)