import sys
sys.stdin = open("b5같은모양찾기.txt")

m = int(input())
arr = []
for i in range(m):
    n = input()
    arr.append(n)

p = int(input())
key1 = ''
key2 = ''
key3 = ''
key4 = ''
for i in range(p):
    key1 += input()
for i in range(p*(p-1),p*p):
    for j in range(0,p*p,p):
        key2 += key1[i-j]
key3 = key1[::-1]
key4 = key2[::-1]

key = []
key.append(key1)
key.append(key2)
key.append(key3)
key.append(key4)

cnt = 0
for i in range(m+1-p):
    for j in range(m+1-p):
        ss = ''
        for k in range(p):
            ss += arr[i+k][j:j+p]
        for keys in key:
            if ss==keys:
                cnt += 1
print(cnt)