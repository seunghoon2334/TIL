import sys
sys.stdin = open("set.txt")

t = int(input())
for tc in range(t):
    data = [1,2,3,4,5,6,7,8,9,10,11,12]
    n, k = map(int, input().split())
    cnt = 0

    for i in range(1 << 12):#2**12번 반복
        a = []
        sum = 0
        for j in range(12):
            if i & (1 << j):
                a.append(data[j])
        if len(a)==n:
            for ii in a:
                sum += ii
            if sum==k:
                cnt += 1
    print(f'#{tc+1} {cnt}')