import sys
sys.stdin = open("input.txt")
def FF(no):
    # 현재 컴퓨터에서 연결되어 있고 감염안된 컴퓨터를 감염시키면서 카운트
    global sol
    for i in range(1, N+1): # 열
        if arr[no][i] and chk[i]==0 :
            chk[i]=1
            sol+=1
            FF(i)
#main --------------------------------
N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)] # 인접행렬
chk = [0]*(N+1)
for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] =1

sol=0
chk[1]=1 # 1번 컴퓨터부터 감염
FF(1) # 1번 컴퓨터부터 시작
print(sol)