import sys
sys.stdin = open('숫자 카운팅.txt')

def search(num):
    if ns[n//2]==num:
        for i in range(0,n):
            if ns[i]==num:
                left = i
                break
        for j in range(n-1,-1,-1):
            if ns[j]==num:
                right = j
                break
    elif ns[n//2] < num:
        for i in range(n//2,n):
            if ns[i]==num:
                left = i
                break
        for j in range(n-1,n//2-1,-1):
            if ns[j]==num:
                right = j
                break
    else:
        for i in range(0,n//2):
            if ns[i]==num:
                left = i
                break
        for j in range(n//1-1,-1,-1):
            if ns[j]==num:
                right = i
                break
    return i, j

n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

s = ''
for i in range(m):
    ij = search(ms[i])
    s += str(ij[1]-ij[0]+1) + ' '
print(s)
