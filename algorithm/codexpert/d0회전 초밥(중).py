n, d, k, c = map(int, input().split())  # 접시수,초밥가짓수,연속접시,쿠폰번호

arr = [0] * n
for i in range(n):
    arr[i] = int(input())

queue = [0] * k
for i in range(k):
    queue[i] = arr[-k + i]

result = len(set(queue))
if c not in queue:
    result += 1

j = 0
for i in range(n):
    queue[j] = arr[i]
    cnt = len(set(queue))
    if c not in queue:
        cnt += 1
    if result < cnt:
        result = cnt
    j += 1
    if j == k:
        j = 0
    if result == k + 1:
        break
print(result)