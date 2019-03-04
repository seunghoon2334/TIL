n, d, k, c = map(int, input().split())  # 접시수,초밥가짓수,연속접시,쿠폰번호

arr = []
for i in range(n):
    arr.append(int(input()))

result = 0
for i in range(n):
    cnt = 0
    arr2 = []
    for ii in range(k):
        tmp = i++ii
        if tmp >= n:
            tmp -= n
        if arr[tmp] not in arr2:
            arr2.append(arr[tmp])
            cnt += 1
    if c not in arr2:
        cnt += 1
    if result < cnt:
        result = cnt
    if result == k + 1:
        break

print(result)