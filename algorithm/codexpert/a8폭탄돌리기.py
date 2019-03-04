k = int(input()) #첫사람
n = int(input()) #퀴즈수
time210 = 0
for nc in range(n):
    time, tfp = input().split()
    time210 += int(time)
    if time210>210:
        break
    if tfp=='T':
        k += 1
        if k>8:
            k=1
print(k)