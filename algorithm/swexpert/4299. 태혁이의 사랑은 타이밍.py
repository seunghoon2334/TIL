import sys
sys.stdin = open('4299.txt')

t = int(input())
for tc in range(1,t+1):
    D, H, M = map(int,input().split()) # 일 시 분
    D0, H0, M0 = 11, 11, 11
    result = 0
    if D < D0 or (D==D0 and H < H0) or (D==D0 and H==H0 and M < M0):
        result = -1
    else:
        if M - M0 < 0:
            H -= 1
            M += 60
        result += M - M0
        if H - H0 < 0:
            D -= 1
            H += 24
        result += 60 * (H - H0)
        result += 1440 * (D - D0)
    print('#{} {}'.format(tc, result))