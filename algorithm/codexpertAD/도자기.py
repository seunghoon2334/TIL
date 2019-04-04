import sys
sys.stdin = open("input.txt")
# 재료별 개수를 정보테이블에 저장하여 재료의 개수만큼 시도
def DFS(no, cnt): # 현재arr[no] 재료의 개수만큼 모두 시도
    global sol, N, M, arr, rec
    if no>=N:
        if cnt==M:
            # for i in range(cnt): print(rec[i], end=' ')
            # print()
            sol+=1
        return
    for i in range(arr[no]+1):#현재료의  개수만큼 시도
        rec[cnt]=i # 개수를 기록
        DFS(no+1, cnt+i)
        rec[cnt]=0
#main --------------------------
T = int(input())
for ti in range(T):
    N, M = map(int, input().split())
    rec = [0]*27 # 재료를 개수별로 담아서 기록하는 배열
    cntarr = [0]*27
    arr = [0] * 27
    temp = list(map(int, input().split()))

    for i in range(N):
        cntarr[temp[i]]+=1
    N =0
    for i in range(27):
        if cntarr[i]:
            arr[N] = cntarr[i]
            N+=1
    sol =0
    DFS(0, 0) #  0 번요소부터 시작, 개수는 0개
    print(sol)

# 이전 재료와 비교하여 다른 재료만 담아보는 시도
# def DFS(start, cnt):
#     global sol, N, M, arr, rec
#     if cnt==M:
#         for i in range(cnt): print(rec[i], end=' ')
#         print()
#         sol+=1
#         return
#     if start >=N : return
#     back=0 # 이전 재료를 백업하여 같은 재료여부 체크
#     for i in range(start, N): #  start부터 끝까지 재료를 담아보는 시도
#         if back == arr[i]: continue
#         rec[cnt]=arr[i]
#         back = arr[i]
#         DFS( i +1 , cnt+1)
#
# #main --------------------------
# T = int(input())
# for ti in range(T):
#     N, M = map(int, input().split())
#     rec = [0]*N # 재료를 개수별로 담아서 기록하는 배열
#     arr = list(map(int, input().split()))
#     arr.sort()
#     sol =0
#     DFS(0, 0) #  0 번요소부터 시작, 개수는 0개
#     print(sol)

