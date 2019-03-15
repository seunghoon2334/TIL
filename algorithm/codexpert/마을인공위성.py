N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))

for h in range(1, N): #높이를 1씩 높여가면서 맵을 반복적으로 탐색
    flag=0
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j]==h:
                flag = 1 #현재 높이가 있으면 체크
                if arr[i-1][j]>=h and arr[i+1][j]>=h and arr[i][j-1]>=h and arr[i][j+1]>=h:
                    arr[i][j]+=1

    if flag==0: break
print (h-1)


