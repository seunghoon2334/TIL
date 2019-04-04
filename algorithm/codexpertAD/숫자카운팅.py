import sys
sys.stdin = open("input.txt")

def lowerSearch(s, e, data): # 왼쪽 끝 경계치 탐색
    sol = -1
    while s<=e:
        m = (s+e)//2
        if data == Narr[m] :# 데이타를 찾으면 왼쪽영역 재탐색
            e = m-1 # 왼쪽영역 탐색
            sol = m # 찾은 위치가 현재 왼쪽 경계치 이므로 백업
        # mid보다 데이타가 크면 오른쪽영역 탐색
        elif data> Narr[m] : s = m+1
        # mid보다 데이타가 작으면 왼쪽영역 탐색
        else : e = m-1
    return sol
def upperSearch(s, e, data): # 오른쪽 끝 경계치 탐색
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if data == Narr[m]: # 데이타를 찾으면 오른쪽영역 재탐색
            s = m + 1  # 오른쪽영역 탐색
            sol = m  # 찾은 위치가 현재 오른쪽 경계치 이므로 백업
        # mid보다 데이타가 크면 오른쪽영역 탐색
        elif data > Narr[m]:
            s = m + 1
        # mid보다 데이타가 작으면 왼쪽영역 탐색
        else: e = m - 1
    return sol
# main ==============================
N = int(input())
Narr = list(map(int, input().split()))
T = int(input())
Tarr = list(map(int, input().split()))
for i in range(T):
    lo = lowerSearch(0, N-1, Tarr[i]) # 왼쪽끝에 위치
    if lo >=0 : # 찾았을 경우만 오른쪽끝 탐색
        up = upperSearch(0, N-1, Tarr[i]) # 오른쪽 끝에 위치
        print(up-lo+1, end=' ')
    else : print(0)




