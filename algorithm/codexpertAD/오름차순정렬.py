import sys
sys.stdin = open("input.txt")

# O(n^2) 단순정렬
def sort(s, e):
    global N
    for i in range(e):
        for j in range(i+1, e+1):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

# O(N log N) Quick sort
def Qsort(s, e):
    if s>=e: return
    P, T = e, s
    for L in range(s, e+1):
        if arr[L]<arr[P]: # 비교는   Left <-> Pivot
            arr[L], arr[T] = arr[T], arr[L] # 교환은 Left <-> Target
            T+=1
    arr[P], arr[T] = arr[T], arr[P]
    Qsort(s, T-1)
    Qsort(T+1, e)

# O(N log N) Merge sort
def Msort(s, e):
    if s>=e: return
    m=(s+e)//2
    Msort(s, m)
    Msort(m+1, e)
    i, j , k = s, m+1, s # i는 왼쪽영역 s~m, j는 오른쪽영역 m+1~e, k는 임시버퍼시작
    while i<=m and j<=e: # 왼족영역, 오른족영역을 나누어서 임시버퍼에 비교한후 저장
        if arr[i]<arr[j]:
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    while i<=m: # 왼쪽영역이 남아있으면 임시버퍼에 저장
        temp[k] = arr[i]
        k += 1
        i += 1
    while j<=e:# 오른쪽영역이 남아있으면 임시버퍼에 저장
        temp[k] = arr[j]
        k += 1
        j += 1
    for i in range(s, e+1): #  임시버퍼를 원버퍼에 저장
        arr[i] = temp[i]

# main ===============================
arr = []
N = int(input())
temp = [0] * N
arr = list(map(int, input().split()))
#arr.sort()
#sort(0, N-1)
#Qsort(0, N-1)
Msort(0, N-1)

for i in range(N):
    print(arr[i], end=' ')



