import sys
sys.stdin = open("1221.txt")

t = int(input())
check = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1,t+1):
    s = input()
    string = list(input().split())
    result = ''
    for i in range(10):
        for _ in range(string.count(check[i])):
            result += check[i] + ' '
    print('#{}'.format(tc))
    print(result)