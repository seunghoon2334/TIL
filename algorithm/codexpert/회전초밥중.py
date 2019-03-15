import sys
sys.stdin = open("in.txt")

N, d, k, c = map(int, input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))

chk = [0]*3001
sol=0
for i in range(N):
    for j in range(k):
        chk[arr[(i+j)%N]]=1
    cnt=0
    if chk[c]==0: cnt=1
    for j in range(1, d+1):
        cnt+=chk[j]
        chk[j]=0
    if cnt>sol: sol=cnt

print(sol)
