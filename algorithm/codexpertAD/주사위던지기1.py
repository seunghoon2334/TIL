import sys
sys.stdin = open("input.txt")


def DFS1(n):
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(1, 7):
        arr[n]=i
        DFS1(n+1)

def DFS3(n):
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(1, 7):
        if chk[i]:continue
        chk[i]=1
        arr[n]=i
        DFS3(n+1)
        chk[i]=0

def DFS2(n, start):
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(start, 7):
        arr[n]=i
        DFS2(n+1, i)

def DFS4(n, start):
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(start, 7):
        arr[n]=i
        DFS4(n+1, i+1)


#main---------------------------------
N, M = map(int, input().split())
arr =[0] * (N+1)
chk = [0] * 7
if M ==1: DFS1(1)
elif M ==3 : DFS3(1)
elif M == 2: DFS2(1, 1)
elif M ==4: DFS4(1,1)
