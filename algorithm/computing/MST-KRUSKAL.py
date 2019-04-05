import sys
sys.stdin = open('최소 신장 트리.txt')
def Find_Set(x):
    if x==p[x]:
        return x
    else:
        return Find_Set(p[x])

def mst():
    global v
    cnt = 0
    total = 0
    i = 0
    while cnt < v:
        p1 = Find_Set(ge[i][0])
        p2 = Find_Set(ge[i][1])
        if p1 != p2:
            total += ge[i][2]
            cnt += 1
            p[p2] = p1
        i += 1
    return total

t = int(input())
for tc in range(1,t+1):
    v, e = map(int,input().split())
    ge = [list(map(int,input().split())) for i in range(e)]
    ge.sort(key=lambda a: a[2])
    p = list(range(v+1))
    gv = [i for i in range(v+1)]
    w = [9999 for _ in range(v+1)]
    print(mst())