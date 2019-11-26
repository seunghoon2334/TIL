import sys
sys.stdin = open('5549.txt')

t = int(input())
for tc in range(1, t+1):
    n = input()[-1]
    if n=='0' or n=='2' or n=='4' or n=='6' or n=='8':
        result = 'Even'
    else:
        result = 'Odd'
    print('#{} {}'.format(tc, result))