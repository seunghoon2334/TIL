for tc in range(1, 11):
    t = int(input())
    tables = []
    for _ in range(t):
        table = list(map(int, input().split()))
        tables.append(table)
    cnt = 0

    for i in range(t):
        p1 = 0
        for j in range(t):
            if tables[j][i] != 0:
                p2 = tables[j][i]
                if p1 == 1 and p2 == 2:
                    cnt += 1
                p1 = p2
    print(f'#{tc} {cnt}')