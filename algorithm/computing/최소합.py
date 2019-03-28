import sys
sys.stdin = open("최소합.txt")

def two(i,j,tmp):
    global result
    tmp += arr[i][j]
    if tmp > result:
        return
    if j!=n-1:
        two(i,j+1,tmp)
    if i!=n-1:
        two(i+1,j,tmp)
    if i==n-1 and j==n-1 and tmp < result:
        result = tmp

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = []
    result = 9999
    for i in range(n):
        arr.append(list(map(int,input().split())))
    two(0,0,0)
    print('#{} {}'.format(tc,result))
