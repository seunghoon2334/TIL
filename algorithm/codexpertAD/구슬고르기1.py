

a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3
M=2
# 1]고르거나 고르지 않는 조합으로 이중재귀로 설계
def DFS1(no, cnt): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
    if no>=N:
        # if cnt==M: # N개중 M개를 고른 조합
        #     for i in range(N): print(b[i], end=' ')
        #     print()
        for i in range(N): print(b[i], end=' ')
        print()
        return
    b[no]=a[no] # 고르기
    DFS1(no+1, cnt+1)
    b[no]=0 # 고르지  않기
    DFS1(no+1, cnt)

# 2] N개를 고르는 조합으로 다중재귀로 설계
def DFS2(start, cnt): # start부터 끝요소까지 고르는 조합
    for i in range(N): print(b[i], end=' ')
    print()

    if cnt>=N or start>=N: return
    for i in range(start, N):
        b[cnt]=a[i]
        DFS2(i+1, cnt+1)
        b[cnt]=0

# main ============================
# 1]고르거나 고르지 않는 조합으로 이중재귀로 설계
#DFS1(0, 0) # b[0]요수에 담기 시작, 구슬시작은  a[0] 부터 시작
# 2] 고르는 조합으로 다중재귀로 설계
DFS2(0, 0) # a[0]요소부터 시작, 고른 개수 0개
