import sys
sys.stdin = open("c8원안의마을.txt")

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
check = [0,1,4,9,16,25,36,49,64,81,100,121,144,169]
for i in range(n):
    s = input()
    cnt = 0
    for j in range(len(s)):
        arr[i][j] = int(s[j])
        if s[j]=='2':
            pointi = i
            pointj = j
        elif s[j]=='1':
            cnt += 1
result = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            a = abs(pointi-i)
            b = abs(pointj-j)
            if a**2 + b**2 > result:
                result = a**2 + b**2
for i in range(len(check)-1):
    if check[i]<=result<=check[i+1]:
        print(i+1)
        break