import sys
sys.stdin = open('4371.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    happy = [0 for _ in range(n)]
    for i in range(n):
        happy[i] = int(input())
    # print(happy)
    visit = [0 for _ in range(n)]
    start = happy[0]
    end = happy[-1]
    cnt = 0
    q = []
    for i in range(1,n):
        key = happy[i] - start
        point = 1 + key
        tmp = 1
        check = [0 for _ in range(n)]
        if visit[i]==0:
            while point <= end and tmp==1:
                if not point in happy:
                    tmp = 0
                    break
                else:
                    check[happy.index(point)] = 1
                point += key
            if tmp==1:
                for ii in range(n):
                    visit[ii] += check[ii]
                cnt += 1
        # print(key,visit)
    print('#{} {}'.format(tc, cnt))