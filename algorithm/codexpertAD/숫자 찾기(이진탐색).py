import sys
sys.stdin = open("숫자 찾기(이진탐색).txt")

def search(start,end,num):
    mid = (start + end)//2
    if num == ns[mid]:
        return mid+1
    elif mid==start or mid==end:
        return 0
    elif num > ns[mid]:
        return search(mid,end,num)
    elif num < ns[mid]:
        return search(start,mid,num)

n = int(input())
ns = list(map(int, input().split()))
t = int(input())
ts = list(map(int, input().split()))

for i in range(t):
    print(search(0,n,ts[i]))
