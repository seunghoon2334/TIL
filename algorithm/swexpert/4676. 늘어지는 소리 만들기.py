import sys
sys.stdin = open('4676.txt')

t = int(input())
for tc in range(1,t+1):
    s = input()
    string = ['' for _ in range(len(s)+1)]
    h = int(input())
    hpoint = list(map(int,input().split()))
    for i in range(h):
        string[hpoint[i]] += '-'
    result = ''
    for i in range(len(s)):
        result += string[i] + s[i]
    print('#{} {}'.format(tc,result+string[-1]))