import sys
sys.stdin = open("view_input.txt")

def max_data(d1, d2, d3, d4):
    maxd = d1
    if maxd < d2:
        maxd = d2
    if maxd < d3:
        maxd = d3
    if maxd < d4:
        maxd = d4
    return maxd

T = 10
for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    result = 0

    for i in range(2,n-2):
        if data[i]>max_data(data[i-2],data[i-1],data[i+1],data[i+2]):
            result += (data[i] - max_data(data[i-2],data[i-1],data[i+1],data[i+2]))

    print(f'#{tc+1} {result}')