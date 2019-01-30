import sys
sys.stdin = open("190130workshop.txt")

# def atoitoa(string):
#     a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#     ss = ''
#     for i in range(10):
#         ss += (a[i] + ' ') * string.count(a[i])
#     return ss
#
# t = int(input())
# for tc in range(t):
#     n = input()
#     s = list(input().split())
#
#     print(f'#{tc+1}')
#     print(atoitoa(s))

def atoitoa(string):
    a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    b = []
    for i in range(len(string)):
        b.append(a.index(string[i]))
    b.sort()
    for i in range(len(b)):
        b[i] = a[b[i]]
    return b

# def atoi(string):
#     a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     b = []
#     for i in range(len(string)):
#         b.append(a.index(string[i]))
#     b.sort()
#     return b
#
#
# def itoa(x):
#     a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     c = []
#     for i in range(10):
#         for ii in range(x.count(i)):
#             c.append(a[i])
#     return c

# def itoa(x):
#     a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     c = []
#     for i in range(len(x)):
#         c.append(a[x[i]])
#     return c

t = int(input())
for tc in range(t):
    n = input()
    s = list(input().split())

    print(f'#{tc+1}')
    print(' '.join(atoitoa(s)))