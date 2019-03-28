import sys
sys.stdin = open('최대 상금.txt')

def myprint(q):
    tt = []
    while q != 0:
        q -= 1
        tt.append(T[q])
    key.append(tt)

def combination(n, r, q):
    if r == 0:
        myprint(q)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        combination(n-1, r-1, q)
        combination(n-1, r, q)

def gogo(arr, cnt):
    global result
    if cnt==0:
        tmp = ''
        for i in arr:
            tmp += i
        if result < int(tmp):
            result = int(tmp)
        return
    else:
        tmp = ''
        for j in arr:
            tmp += j
        if int(tmp) not in check[cnt-1]:
            check[cnt-1].append(int(tmp))
            for i in range(len(key)):
                arr[key[i][0]],arr[key[i][1]] = arr[key[i][1]], arr[key[i][0]]
                gogo(arr,cnt-1)
                arr[key[i][0]], arr[key[i][1]] = arr[key[i][1]], arr[key[i][0]]

t = int(input())
for tc in range(1,t+1):
    money, count = input().split()
    marr = []
    for i in money:
        marr.append(i)
    count = int(count)
    lm = len(money)
    A = [i for i in range(lm)]
    T = [0] * lm
    key = []
    combination(lm, 2, 2)
    result = 0
    check = [[] for _ in range(count)]
    gogo(marr,count)
    print('#{} {}'.format(tc,result))