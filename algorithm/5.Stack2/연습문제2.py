def process_solution(a, k):
    global cnt
    result = []
    for i in range(k,0,-1):
        if a[i] :
            result.append(data[i])
    cnt += 1
    return result

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        check = process_solution(a, k) #답이면 원하는 작업
        tmp = 10
        for i in range(len(check)):
            tmp -= check[i]
            if tmp<0:
                break
        if tmp==0:
            total_cnt += 1
            print(check[::-1])
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 10)
print(cnt)
print(total_cnt)