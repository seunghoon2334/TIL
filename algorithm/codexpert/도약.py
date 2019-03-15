import sys
sys.stdin = open("in.txt")

N = int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))
arr.sort()
print(arr)
cnt=0
for i in range(N-2):
    for j in range(i+1, N-1):
        jump1 = arr[j]-arr[i]
        for k in range(j+1, N):
            jump2 = arr[k]-arr[j]
            if jump1 <= jump2 <=jump1*2 :
                cnt+=1

print(cnt)