import sys
sys.stdin = open("2805.txt")

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        s = input()
        arr2 = []
        for i in s:
            arr2.append(int(i))
        arr.append(arr2)
    center = n//2
    result = 0
    for i in range(center+1):
        for j in range(center+1):
            result += arr[i+j][center-i+j]
    for i in range(center):
        for j in range(center):
            result += arr[i+j+1][center-i+j]
    print('#{} {}'.format(tc,result))