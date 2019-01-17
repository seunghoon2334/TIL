import sys
sys.stdin = open("minmax.txt")

def mm(length, data):
    min = data[0]
    max = data[0]
    for i in range(1,length):
        if min > data[i]:
            min = data[i]
        if max < data[i]:
            max = data[i]
    return max - min

n = int(input())
for i in range(n):
    t = int(input())
    tc = list(map(int, input().split()))
    result = mm(t, tc)
    print(f'#{i+1} {result}')