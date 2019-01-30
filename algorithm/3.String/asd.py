import sys
sys.stdin = open("190130workshop.txt")


def atoitoa(string):
    a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    ss = ''
    for i in range(10):
        ss += (a[i] + ' ') * string.count(a[i])
    return ss

t = int(input())
for tc in range(t):
    s = list(input().split())

    print(f'#{tc+1}')
    print(atoitoa(s))