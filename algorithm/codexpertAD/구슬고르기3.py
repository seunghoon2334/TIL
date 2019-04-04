import sys
sys.stdin = open("input.txt")


a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
chk = [0, 0, 0] # 구슬 사용여부 체크
N = 3
M=2
# 1]구슬 중복을 배제하여 N개중 N개 고르는 순열구조
def DFS1(no):
    if no>=N:
        for i in range(N): print(b[i], end=' ')
        print()
        return
    for i in range(N): #  a[i] 구슬을 고르는 경우의 수(중복배제)
        if chk[i]: continue
        chk[i]=1
        b[no]=a[i]
        DFS1(no+1)
        chk[i]=0
# 2] 구슬 중복을 배제하여 N개중 M개 고르는 순열구조
def DFS2(no, cnt):
    if cnt==M:
        for i in range(N): print(b[i], end=' ')
        print()
        return
    if no>=N: return
    for i in range(N):
        if chk[i]: continue
        chk[i]=1
        b[no]=a[i]
        DFS2(no+1, cnt+1)
        chk[i]=0
        b[no]=0
# 3] 구슬 중복 사용하여 N개 고르는 순열구조
def DFS3(no):
    if no>=N:
        for i in range(N): print(b[i], end=' ')
        print()
        return
    for i in range(N):
        b[no]=a[i]
        DFS3(no+1)

# main ============================
# 1] 구슬 중복을 배제하여 N개중 N개 순열구조
# DFS1(0) # b[0]요소부터 담기 시작
# 2] 구슬 중복을 배제하여 N개중 M개 순열구조
# DFS2(0, 0) # # b[0]요소부터 담기 시작, 개수 0개
# 3] 구슬 중복 사용하여 N개 고르는 순열구조
DFS3(0)
