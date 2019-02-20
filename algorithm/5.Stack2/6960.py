import sys
sys.stdin = open("6960.txt")

t = int(input())
for tc in range(t):
    n = int(input())
    s = []
    f = []
    problem = []
    problem2 = []
    for i in range(n):
        si, fi = map(int, input().split())
        s.append(si)
        f.append(fi)
        problem.append([fi,si])
        problem2.append([si, fi])
    problem.sort()
    problem2.sort()
    check = [0 for _ in range(len(problem))]
    time = 0
    cnt = 0
    for i in range(len(problem)):
        time += problem[i][1]
        if problem[i][0]>=time and check[i]==0:
            cnt += 1
            check[i] = 1
        else:
            time -= problem[i][1]
        for ii in range(i,len(problem)):
            time += problem[ii][1]
            if problem[ii][0] >= time and check[ii] == 0:
                cnt += 1
                check[ii] = 1
            else:
                time -= problem[ii][1]
    cnt2 = 0
    time2 = 0
    for i in range(len(problem2)):
        time2 += problem2[i][0]
        if time2 <= problem2[i][1]:
            cnt2 += 1


    print(problem)
    print(problem2)
    print(check)
    print(f'#{tc+1} {max(cnt,cnt2)}')