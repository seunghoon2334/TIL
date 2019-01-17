import sys
sys.stdin = open("card.txt")

def cntn(data):
    c = [0] *10
    for i in range(len(data)):
        c[int(data[i]) % 10] += 1
    return c

def maxn(data):
    max1 = int(data[0][0])
    num = 0
    for i in range(1,len(data[0])):
        if int(data[0][i]) >= max1:
            max1 = int(data[0][i])
            num = i
    return num, max1

n = int(input())
for i in range(n):
    t = int(input())
    num = input()
    print(f'#{i+1} {maxn(cntn(num))[0]} {maxn(cntn(num))[1]}')