import sys
sys.stdin = open("190117workshop.txt")

def maxm(data):
    mx = data[0]
    for i in range(len(data)):
        if mx < data[i]:
            mx = data[i]
    return mx

def minm(data):
    mn = 50
    for i in range(len(data)):
        if data[i]==0:
            pass
        elif mn > data[i]:
            mn = data[i]
    return mn

def indexsearch(data, num):
    for i in range(len(data)):
        if data[i]==num:
            return i
    return None

for i in range(10):
    n = int(input())
    box = list(map(int, input().split()))
    cnt = 0
    for ii in range(n):
        a = indexsearch(box, maxm(box))
        b = indexsearch(box, minm(box))
        if maxm(box) - minm(box) > 1:
            box[a] -= 1
            box[b] += 1
        else :
            break
    print(f'#{i+1} {maxm(box)-minm(box)}')