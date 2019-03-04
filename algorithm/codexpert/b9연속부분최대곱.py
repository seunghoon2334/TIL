import sys
sys.stdin = open("b9연속부분최대곱.txt")

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = float(input())

# tmp = arr[0]
# result = arr[0]
# for i in range(1,n):
#     if tmp * arr[i] > 1:
#         tmp *= arr[i]
#     else:
#         tmp = arr[i]
#     if result < tmp:
#         result = tmp
#
# print("%0.3f" %result)

tmp1 = 1
tmp2 = arr[0]
result = 0
for i in range(n):
    tmp2 = arr[i]
    tmp1 = max(tmp1*arr[i], tmp2)
    if tmp1>result:
        result = tmp1
print("%0.3f" %result)