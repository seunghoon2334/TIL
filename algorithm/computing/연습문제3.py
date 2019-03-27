# {1,2,3}
count = 0
N = 10
A = [0 for _ in range(N)]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n):
    global count
    count += 1
    s = []
    for i in range(n):
        if A[i] == 1:
            s.append(data[i])
            if sum(s)>10:
                break
    if sum(s)==10:
        print(' '.join(map(str,s)))

def powerset(n,k):
    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)

powerset(N, 0)