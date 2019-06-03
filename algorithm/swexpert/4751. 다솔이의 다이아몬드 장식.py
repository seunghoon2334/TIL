import sys
sys.stdin = open('4751.txt')

t = int(input())
for tc in range(1, t+1):
    s = input()
    ls = len(s)
    s1 = '..#.'
    s2 = '.#.#'
    s3 = '#'
    s4 = '.'

    result1 = s1*ls + s4
    result2 = s2*ls + s4
    result3 = s3
    for i in range(ls):
        result3 += '.' + s[i] + '.#'

    print(result1)
    print(result2)
    print(result3)
    print(result2)
    print(result1)