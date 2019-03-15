import sys
sys.stdin = open("in.txt")

arr = [0]*100001  # 소수는 0, 소수아니면 1로 체크
def aretos(e): #에레토스테네스의 체
    for i in range(2, e+1): # 배수
        if arr[i]: continue # 이미 체크됐으면 스킵
        if i*i>e: break # 루트값까지만 배수 시도
        for j in range(i*2, e+1, i):
            arr[j]=1 # 배수값들을 체크

a, b = map(int, input().split())
if a>b:
    a, b = b, a
arr[1]=1
aretos(b)

cnt=0
for i in range(a, b+1):
    if arr[i]==0:
        cnt+=1

for i in range(a, b+1):
    if arr[i]==0:
        break
smin=i

for i in range(b, a+1, -1):
    if arr[i]==0:
        break
smax=i

print(cnt)
print(smax + smin)


