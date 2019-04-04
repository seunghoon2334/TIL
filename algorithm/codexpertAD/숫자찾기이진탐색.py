import sys
sys.stdin = open("input.txt")

def binSearch(s, e, data):
    while s<=e:
        m = (s+e)//2
        # mid번째값이 찾을 데이타이면 찾은위치+1 를 리턴
        if data == Narr[m]: return m +1
        # mid번째값 보다 데이타가 크면 오른쪽 영역 탐색
        elif data > Narr[m] : s = m+1
        # mid번째값 보다 데이타가 작으면 왼쪽 영역 탐색
        else: e = m-1
    # 못찾으면 0리턴
    return 0

# main ==============================
N = int(input())
Narr = list(map(int, input().split()))
T = int(input())
Tarr = list(map(int, input().split()))

for i in range(T):
    print ( binSearch(0, N-1, Tarr[i]) )

