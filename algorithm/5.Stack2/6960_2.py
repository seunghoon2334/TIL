import sys
sys.stdin = open("6960.txt")

def powerset(arr):
    result = []
    for i in range(1 << len(arr)):
        check = [0 for _ in range(len(arr))]
        for j in range(len(arr)):
            if i & (1 << j):
                check[j] = 1
        result.append(check)
    return result

t = int(input())
for tc in range(t):
    n = int(input())
    s = []
    f = []
    for i in range(n):
        si, fi = map(int, input().split())
        s.append(si)
        f.append(fi)
    result = powerset(s)
    points = []
    cnts = []
    mf = max(f)
    for i in range(len(result)):
        point = 0
        cnt = 0
        for ii in range(n):
            pp = result[i][ii] * s[ii]
            if pp!=0:
                point += pp
                cnt += 1
        points.append(point)
        cnts.append(cnt)
    for i in range(len(points)):
        if points[i]>mf:
            points[i]=0
    print(f'#{tc+1} {cnts[points.index(max(points))]}')