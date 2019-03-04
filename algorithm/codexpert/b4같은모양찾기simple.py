import sys
sys.stdin = open("b4같은모양찾기simple.txt")

m = int(input())
arr = []
for i in range(m):
    n = input()
    arr.append(n)

p = int(input())
key = ''
for i in range(p):
    key += input()

cnt = 0
for i in range(m+1-p):
    for j in range(m+1-p):
        ss = ''
        for k in range(p):
            ss += arr[i+k][j:j+p]
        if ss==key:
            cnt += 1
print(cnt)