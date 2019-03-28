import sys
sys.stdin = open('컨테이너 운반.txt')

def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] >= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split()) # 컨테이너수 트럭수
    w = list(map(int,input().split())) # 컨테이너무게
    t = list(map(int,input().split())) # 트럭 적재용량
    w = merge_sort(w)
    t = merge_sort(t)
    # w.sort(reverse=True)
    # t.sort(reverse=True)

    result = 0
    cnt = 0
    for i in range(m):
        if w[cnt] <= t[i]:
            result += w[cnt]
        else:
            while cnt!=n-1:
                cnt += 1
                if w[cnt] <= t[i]:
                    result += w[cnt]
                    break
        cnt += 1
        if cnt==n:
            break
    print('#{} {}'.format(tc,result))