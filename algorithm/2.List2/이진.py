import sys
sys.stdin = open("binary.txt")

t = int(input())
for tc in range(t):
    p, pa, pb = map(int, input().split())

    left = 1
    right = p
    center = int((left + right) / 2)
    cnta = 0
    while center!=pa:
        cnta += 1
        if center < pa:
            left = center
        elif center > pa:
            right = center
        center = int((left + right) / 2)

    left = 1
    right = p
    center = int((left + right) / 2)
    cntb = 0
    while center!=pb:
        cntb += 1
        if center < pb:
            left = center
        elif center > pb:
            right = center
        center = int((left + right) / 2)

    if cnta > cntb:
        print(f'#{tc+1} B')
    elif cnta < cntb:
        print(f'#{tc + 1} A')
    else:
        print(f'#{tc + 1} 0')