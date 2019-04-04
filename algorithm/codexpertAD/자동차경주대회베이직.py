
import sys
sys.stdin = open("input.txt")
# def DFS(no, dsum, tsum):
#     global sol
#     if dsum + dist[no]>limit: return
#     if no>=N:
#         if tsum<sol: sol=tsum
#         return
#     DFS(no+1, dsum+dist[no], tsum) # 정비를 받지 않기
#     DFS(no+1, 0, tsum+time[no]) # 정비를 받기
# # main -------------------------------
# limit=int(input())
# N = int(input())
# dist = list(map(int, input().split()))
# time = list(map(int, input().split()))
# sol=0x7fffffff
# DFS(0, 0, 0) # 0번 정비소부터, 거리 0, 시간0
# print(sol)





def DFS(start, tsum):
    global sol
    if tsum>sol: return
    if start>N:
        if tsum<sol: sol=tsum
        return
    tot=0 #거리 누적
    # 출발점에서 제한된 거리 이내에서 모두 정비를 받아보는 경우의 수 시도
    for i in range(start, N+1):
        if tot + dist[i]>limit: break # 거리벗어나면 탈출
        tot+=dist[i]
        DFS(i+1, tsum+time[i])

#main -------------------------
limit = int(input())
N = int(input())
dist = list(map(int, input().split()))
time = list(map(int, input().split()))
time.append(0)
sol = 0x7fffffff
DFS(0, 0)
print(sol)