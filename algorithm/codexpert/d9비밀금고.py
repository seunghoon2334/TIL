import sys
sys.stdin = open("d9비밀금고.txt")

n = int(input())
arr = [[0 for _ in range(2*n-1)] for _ in range(2*n-1)]

result = [0 for _ in range(2*n-1)]

start = (2*n-1)//2
end = (2*n-1)//2+1
key = list(map(int, input().split()))
tmp = 1
check = 0
for i in range(2*n-1):
    for j in range(start,end,2):
        result[j] += key[check]
        check += 1

    start -= tmp
    end += tmp
    if start==0:
        tmp = -1
print(max(result))