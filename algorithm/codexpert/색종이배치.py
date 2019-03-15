
r, c, w, h = map(int, input().split())
arr = [[0]*100 for i in range(100)]

# 첫번째 색종이 붙이기
for i in range(r-1, r+h+1):
    for j in range(c-1, c+w+1):
        if i==r-1 or i==r+h or j==c-1 or j == c+w:
            arr[i][j]=2 #가장자리 마킹
        else:
            arr[i][j]=1 # 색종이 마킹
for i in range(30):
    for j in range(30):
        print(arr[i][j], end=' ')
    print()



