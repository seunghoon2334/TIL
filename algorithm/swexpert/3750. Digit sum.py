import sys
sys.stdin = open('3750.txt')

def digit_sum(n):
    tmp = sum(map(int, ' '.join(n).split()))
    return str(tmp)

t = int(input())
result = [[] for _ in range(t)]
for tc in range(t):
    n = input()
    while len(n)!=1:
        n = digit_sum(n)
    result[tc] = '#{} {}'.format(tc+1, n)
print('\n'.join(result))