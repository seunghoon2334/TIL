
def clear(i):
    for j in range(N):
        dist = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1]-arr[j][1])
        if dist<=R:
            arr[j][2]-=P

def update(i):
    for j in range(N):
        dist = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1]-arr[j][1])
        if dist<=R: arr[j][2]+=P

def DFS(no): # 현재 미사일로 침몰하지 않은 모든 군함에 쏘아보는 경우 시도
    global sol
    if no>M:
        cnt=0
        for i in range(N):
            if arr[i][2]>0: cnt+=1 # 살아남은 군함의 개수
        if cnt<sol: sol=cnt
        return

    for i in range(N):
        if arr[i][2]<=0 : continue # 침몰한 군함은 스킵
        clear(i) # i군함 반경이내 모든 군함 에너지 차감
        DFS(no+1)
        update(i) # i군한 반경이내 모든 군함 에너지 복원

#main -------------------------
N= int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
M, P, R = map(int, input().split())

sol=16
DFS(1)
print(sol)

