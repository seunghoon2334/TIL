def process_solution(a, k, sum):
    if sum > key : return
    global cnt
    point = 0
    ppoint = 0
    for i in range(1, k+1):
        if a[i] :
            point += data[i]
            ppoint += 1
    if point<=key:
        pp.append(ppoint)

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input, sum):
    if sum > key : return

    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum) #답이면 원하는 작업
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            if a[k]:
                backtrack(a, k, input, sum + data[k])
            else:
                backtrack(a, k, input, sum)
    total_cnt += 1

global key, pp
key = 5
pp = []
MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 10, 0)
print(pp)


