import sys
sys.stdin = open('3314.txt')

t = int(input())
for tc in range(1,t+1):
    score = list(map(int, input().split()))
    num = len(score)
    total = 0
    for i in range(num):
        point = score[i]
        if point > 40:
            total += point
        else:
            total += 40
    print('#{} {}'.format(tc,total//num))