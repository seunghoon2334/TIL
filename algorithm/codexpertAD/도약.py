import sys
sys.stdin = open("input.txt")

def lowerSearch(s, e, data): # 왼쪽 끝 경계치 탐색
    sol = -1
    while s<=e:
        m = (s+e)//2
        if arr[m] >= data : #mid가 데이타 이상이면 더 작은 값 탐색 위해 왼쪽영역 탐색
            e = m-1 # 왼쪽영역 탐색
            sol = m # 찾은 위치 백업
        else : s = m+1
    return sol
def upperSearch(s, e, data): # 오른쪽 끝 경계치 탐색
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if arr[m] <= data:  # mid가 데이타 이하이면 더 큰 값 탐색 위해 오른쪽영역 탐색
            s = m + 1  # 오른쪽영역 탐색
            sol = m  # 찾은 위치 백업
        else: e = m - 1
    return sol
# main ==============================
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

cnt=0
for i in range(N-2): #출발위치
    for j in range(i+1, N-1): # 첫번째 점프
        dist = arr[j] - arr[i]
        start = arr[j] + dist
        end = arr[j] + dist*2
        lo = lowerSearch(j+1, N-1, start)# 두번째 점프 시작값 이상중 작은 값 위치
        # 예외조건 : 못찾을 경우 또는 2배 초과시 스킵
        if lo==-1 or arr[lo]>end: continue
        up = upperSearch(j+1, N-1, end)# 두번째 점프 끝값 이하중 큰 값의 위
        cnt += (up-lo+1)

print(cnt)



