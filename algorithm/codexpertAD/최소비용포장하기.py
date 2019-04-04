import sys
sys.stdin = open("input.txt")

# main ==============================
N = int(input())
arr = list(map(int, input().split()))

sol=0
for k in range (N-1):
    # 2개만 정렬하기
    for i in range(k, k+2):
        for j in range(i+1, N):
            if arr[i]> arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    # 앞에서 2개 포장하여 저장
    arr [k+1] += arr[k]
    # 포장비용 누계
    sol += arr[k+1]
print(sol)
