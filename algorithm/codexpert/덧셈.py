
import sys
sys.stdin = open("in.txt")

num, X = input().split()
X = int(X)
N=len(num)
flag=0
for i in range(N-1):
    A = int(num[:i+1])
    B = int(num[i+1:N])
    if A+B == X :
        flag=1
        break
if flag ==1:
    print('%d+%d=%d' % (A, B, X))
else:
    print('NONE')

#3 개로 분리
# for i in range(N-2):
#     A = int(num[:i+1])
#     for j in range(i+1, N-1):
#         B = int (num[i+1:j+1])
#         C = int (num[j+1:N])
#         print(A, B, C)


