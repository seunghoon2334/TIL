import sys
sys.stdin = open("in.txt")

N = int(input())
arr = []
for i in range(N):
    arr.append(float(input()))

mul = 1.0
max = 0.0
# for i in range(N):
#     mul=1.0
#     for j in range(i, N):
#         mul *= arr[j]
#         if mul>max :
#             max=mul
#
# print('%.3f' % max)

for i in range(N):
    if mul*arr[i] < arr[i]: #현재수보다 작으면 현재수부터시작
        mul = arr[i]
    else:
        mul *= arr[i]
    if mul>max:
        max=mul
print('%.3f' % max)









