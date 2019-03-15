# 폭탄돌리기


K = int(input())
N = int(input())
tot = 0

for i in range(N):
    T, quiz = input().split()
    T = int(T)
    tot += T
    if tot > 210:
        break
    if quiz is 'T':
        K = (K % 8) + 1
if tot <= 210:
    print(K - 1)
else:
    print(K)


