import sys
sys.stdin = open('최소 비용으로 포장 다시하기.txt')

def candy(n,ns,cnt):
    global result
    if n==1:
        return 0
    elif n==2:
        result += ns[cnt] + ns[cnt+1]
        return
    else:
        result += ns[cnt] + ns[cnt+1]
        ns[cnt+1] += ns[cnt]
        cnt += 1
        for i in range(cnt,n-2):
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
            else:
                break
        return candy(n-1,ns,cnt)

n = int(input())
ns = list(map(int,input().split()))
result = 0
candy(n,ns,0)
print(result)